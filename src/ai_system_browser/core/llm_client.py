"""Ollama LLM Client für lokale Sprachmodell-Inferenz."""

import ollama
from typing import List, Dict, Optional, AsyncGenerator
from loguru import logger
import asyncio


class OllamaClient:
    """Client für Ollama-LLM Integration.
    
    Ermöglicht die Kommunikation mit lokal gehosteten LLMs über Ollama.
    Unterstützt verschiedene Modelle wie Mistral, Llama 3, etc.
    """
    
    def __init__(
        self,
        model: str = "mistral:7b",
        host: str = "http://localhost:11434",
        temperature: float = 0.7,
        max_tokens: int = 2048
    ):
        """Initialisiert den Ollama Client.
        
        Args:
            model: Name des zu verwendenden Modells
            host: Ollama Server URL
            temperature: Sampling Temperature (0.0-1.0)
            max_tokens: Maximale Anzahl von Tokens in der Antwort
        """
        self.model = model
        self.host = host
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.client = ollama.Client(host=host)
        logger.info(f"Ollama Client initialisiert mit Modell: {model}")
    
    def generate(self, prompt: str, system: Optional[str] = None) -> str:
        """Generiert eine Antwort auf den gegebenen Prompt.
        
        Args:
            prompt: Der Eingabe-Prompt
            system: Optionale System-Nachricht
            
        Returns:
            Die generierte Antwort als String
        """
        try:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            messages.append({"role": "user", "content": prompt})
            
            response = self.client.chat(
                model=self.model,
                messages=messages,
                options={
                    "temperature": self.temperature,
                    "num_predict": self.max_tokens
                }
            )
            
            answer = response['message']['content']
            logger.debug(f"LLM Antwort erhalten: {len(answer)} Zeichen")
            return answer
            
        except Exception as e:
            logger.error(f"Fehler bei LLM-Generierung: {e}")
            raise
    
    async def generate_stream(
        self,
        prompt: str,
        system: Optional[str] = None
    ) -> AsyncGenerator[str, None]:
        """Streamt die Antwort token-by-token.
        
        Args:
            prompt: Der Eingabe-Prompt
            system: Optionale System-Nachricht
            
        Yields:
            Einzelne Tokens der Antwort
        """
        try:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            messages.append({"role": "user", "content": prompt})
            
            stream = self.client.chat(
                model=self.model,
                messages=messages,
                stream=True,
                options={
                    "temperature": self.temperature,
                    "num_predict": self.max_tokens
                }
            )
            
            for chunk in stream:
                if 'message' in chunk:
                    content = chunk['message'].get('content', '')
                    if content:
                        yield content
                        
        except Exception as e:
            logger.error(f"Fehler beim Streaming: {e}")
            raise
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict]] = None
    ) -> Dict:
        """Führt einen Multi-Turn Chat durch.
        
        Args:
            messages: Liste von Chat-Nachrichten
            tools: Optionale Tool-Definitionen für Function Calling
            
        Returns:
            Die Antwort mit Metadaten
        """
        try:
            response = self.client.chat(
                model=self.model,
                messages=messages,
                tools=tools,
                options={
                    "temperature": self.temperature,
                    "num_predict": self.max_tokens
                }
            )
            return response
            
        except Exception as e:
            logger.error(f"Fehler beim Chat: {e}")
            raise
    
    def check_model_availability(self) -> bool:
        """Prüft ob das Modell verfügbar ist.
        
        Returns:
            True wenn Modell verfügbar, sonst False
        """
        try:
            models = self.client.list()
            available_models = [m['name'] for m in models.get('models', [])]
            is_available = self.model in available_models
            
            if not is_available:
                logger.warning(
                    f"Modell {self.model} nicht verfügbar. "
                    f"Verfügbare Modelle: {available_models}"
                )
            return is_available
            
        except Exception as e:
            logger.error(f"Fehler bei Modellprüfung: {e}")
            return False
    
    def pull_model(self) -> bool:
        """Lädt das Modell herunter falls nicht vorhanden.
        
        Returns:
            True bei Erfolg, sonst False
        """
        try:
            logger.info(f"Lade Modell {self.model} herunter...")
            self.client.pull(self.model)
            logger.info(f"Modell {self.model} erfolgreich geladen")
            return True
            
        except Exception as e:
            logger.error(f"Fehler beim Laden des Modells: {e}")
            return False
