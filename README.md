# AI-System Browser

## Überblick

AI-System Browser ist ein Open-Source-KI-Agenten-System für Debian/Ubuntu, das fortschrittliche AI-Funktionalitäten nachbildet. Das Projekt zielt darauf ab, eine vollständig kostenlose Alternative zu entwickeln, die auf lokalen Ressourcen (CPU/RAM) basiert und keine Cloud-APIs oder dedizierte GPUs erfordert.

## Hauptfunktionen

- **Autonome Aufgabenverwaltung**: Interpretation komplexer Anweisungen, Zerlegung in Unterschritte und Orchestrierung der Ausführung
- **Sandbox-Umgebung**: Sichere Ausführung von Code (Python, Node.js) und Shell-Befehlen mit Dateisystemzugriff
- **Integrierter Browser**: Steuerung eines Webbrowsers für Recherche, Interaktion und Transaktionen
- **Mediengenerierung**: Kostenlose, RAM-basierte Bilderzeugung
- **Multi-modale Fähigkeiten**: Verarbeitung und Erstellung von Text, Code, Daten und Bildern

## Technologie-Stack

### Agenten-Kern
- **Framework**: AutoGen (Microsoft)
- **LLM-Inferenz**: Ollama
- **Modelle**: Mistral 7B / Llama 3 8B (quantisierte GGUF-Modelle)

### Tool-Schicht
- **Sandbox**: Docker
- **Browser-Automatisierung**: Playwright
- **UI**: Electron
- **Bilderzeugung**: Stable Diffusion mit CPU-optimierten Engines (FastSD CPU / SD.cpp)

## Systemanforderungen

- **Betriebssystem**: Debian oder Ubuntu
- **RAM**: Mindestens 16 GB, empfohlen 32 GB oder mehr
- **CPU**: Moderne Multi-Core-CPU
- **Festplatte**: Mindestens 20 GB freier Speicherplatz

## Dokumentation

Dieses Repository enthält umfassende Planungsdokumente für das Projekt:

- **Umfassender Plan**: Detaillierte Beschreibung der Architektur und Implementierung
- **Technisches Konzept**: Architekturbersicht und Komponentenbeschreibung
- **Technologie-Stack**: Auswahl und Begründung der verwendeten Open-Source-Technologien
- **Machbarkeitsstudie**: Analyse der RAM-basierten Bilderzeugung

## Projektphase

Das Projekt befindet sich derzeit in der Planungs- und Konzeptionsphase. Die Dokumentation umfasst:

1. Funktionsanalyse
2. Architekturbersicht
3. Technologie-Auswahl und -Begründung
4. Machbarkeitsstudie zur CPU-basierten Bilderzeugung
5. Implementierungsplan

## Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## Beitragen

Beiträge sind willkommen! Bitte öffnen Sie ein Issue oder einen Pull Request.

## Hintergrund

Das Projekt wurde als kostenlose Open-Source-Alternative entwickelt, um volle Kontrolle über das System zu behalten und gleichzeitig fortschrittliche AI-Agenten-Funktionalitäten bereitzustellen.
