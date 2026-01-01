"""AI-System Browser - Open Source KI-Agenten-System.

Ein modulares System zur Automatisierung komplexer Aufgaben durch
KI-Agenten mit Browser-Kontrolle, Sandbox-Ausführung und
lokaler LLM-Integration.
"""

__version__ = "0.1.0"
__author__ = "Tech-lab-sys"
__license__ = "MIT"

from .core.agent_system import AgentSystem
from .core.llm_client import OllamaClient
from .browser.controller import BrowserController
from .sandbox.docker_manager import DockerSandbox

__all__ = [
    "AgentSystem",
    "OllamaClient",
    "BrowserController",
    "DockerSandbox",
]
