# 🛠️ Astralis CLI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&style=flat-square)
![Docker](https://img.shields.io/badge/Docker-orchestration-2496ED?logo=docker&style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

**Command-line tool for managing Docker containers and servers**  
Simplify your DevOps workflow with intuitive commands for container management, system monitoring, and server administration.

[🚀 Installation](#-installation) • [📖 Usage](#-usage) • [🛠️ Tech Stack](#️-tech-stack)

</div>

---

## ✨ Features

### 🐳 Docker Management
- List all containers with status
- Start/stop/restart containers
- View container logs
- Monitor resource usage (CPU, RAM)

### 🖥️ System Monitoring
- Real-time CPU, RAM, disk usage
- Temperature monitoring
- Process list
- Uptime and load average

### ⚡ Quick Actions
- Reboot/shutdown server
- Clear Docker cache
- Backup containers config
- Health check all services

### 🎨 Beautiful Output
- Colored terminal output
- Progress bars
- Tables for data display
- Emoji indicators

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.11+** | Core language |
| **rich** | Terminal UI and colors |
| **docker-py** | Docker API client |
| **click** | CLI framework |
| **psutil** | System monitoring |

---

## 📦 Installation

```bash
git clone https://github.com/Fioru12/Astralis-CLI.git
cd Astralis-CLI
pip install -r requirements.txt
```

### Global Install
```bash
pip install -e .
astralis-cli --help
```

---

## 📖 Usage

### Docker Commands
```bash
# List all containers
astralis-cli docker list

# Start/stop/restart
astralis-cli docker start nginx
astralis-cli docker stop nginx
astralis-cli docker restart nginx

# View logs
astralis-cli docker logs nginx --tail 50

# Monitor resources
astralis-cli docker stats
```

### System Commands
```bash
# System info
astralis-cli system info

# Monitor resources
astralis-cli system monitor

# Process list
astralis-cli system processes

# Temperature
astralis-cli system temp
```

### Quick Actions
```bash
# Reboot server
astralis-cli server reboot

# Clear Docker cache
astralis-cli docker clean

# Health check
astralis-cli health check
```

---

## 🏗️ Architecture

```
Astralis-CLI/
├── astralis_cli/
│   ├── __init__.py
│   ├── cli.py              # Main CLI entry point
│   ├── commands/
│   │   ├── docker.py       # Docker commands
│   │   ├── system.py       # System commands
│   │   └── server.py       # Server commands
│   ├── utils/
│   │   ├── display.py      # Rich UI helpers
│   │   └── helpers.py      # Utility functions
│   └── config.py           # Configuration
├── tests/
│   └── test_cli.py
├── requirements.txt
├── setup.py
├── Dockerfile
└── README.md
```

---

## 🧪 Testing

```bash
pytest tests/ -v
```

---

## 📈 Roadmap

- [ ] Add support for Kubernetes
- [ ] Implement plugin system
- [ ] Add configuration file support
- [ ] Shell completion (bash, zsh, fish)
- [ ] Interactive mode
- [ ] Remote server support (SSH)

---

## 🤝 Contributing

Contributions are welcome! Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Fioru12** - [GitHub Profile](https://github.com/Fioru12)

---

<div align="center">
  <sub>Built with ❤️ for efficient server management</sub>
</div>
