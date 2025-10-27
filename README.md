# Enterprise AI Agent - Production-Ready Multi-Tool Agent System

A comprehensive, production-ready AI agent implementation using LangChain, OpenAI, and enterprise-grade architecture patterns. This repository demonstrates how to build autonomous agents that can reason, plan, and execute complex multi-step workflows.

## 🎯 Overview

This project implements a **ReAct (Reasoning + Acting)** agent with:
- **Multi-tool integration** (web search, database, file operations)
- **Persistent memory** using vector embeddings
- **Production-grade error handling** and retry logic
- **Comprehensive monitoring** and observability
- **Security controls** and input validation
- **Docker deployment** ready

## 📚 Tutorial Article

This code accompanies the comprehensive tutorial article:
**["Building Production-Ready AI Agents with Multi-Tool Integration"](https://crashbytes.com/articles/building-production-ai-agents-multi-tool-langchain-openai-enterprise-automation-2025)**

## ✨ Features

### Core Capabilities
- ✅ **ReAct Agent Architecture**: Iterative reasoning and action execution
- ✅ **Multi-Tool Integration**: Web search, database queries, file operations
- ✅ **Vector Memory**: Semantic search across conversation history
- ✅ **Task Planning**: Automatic decomposition of complex goals
- ✅ **Dependency Management**: Respects task prerequisites
- ✅ **Error Resilience**: Graceful degradation and retry logic

### Production Features
- ✅ **Structured Logging**: Comprehensive audit trail with Loguru
- ✅ **Metrics Collection**: Prometheus-compatible performance tracking
- ✅ **Cost Tracking**: Monitor and control LLM API costs
- ✅ **Input Validation**: Security controls with Pydantic
- ✅ **Rate Limiting**: API throttling and retry mechanisms
- ✅ **Docker Support**: Containerized deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or later
- OpenAI API key
- Brave Search API key (optional, for web search)
- PostgreSQL (optional, for database tool)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/CrashBytes/enterprise-ai-agent.git
cd enterprise-ai-agent
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

5. **Run the agent**
```bash
# Interactive mode
python -m src.main interactive

# Single goal execution
python -m src.main run "Research the top 3 AI trends for 2025"
```

## 📁 Project Structure

```
enterprise-ai-agent/
├── src/
│   ├── agent/              # Agent core logic
│   │   ├── react_agent.py  # ReAct implementation
│   │   └── state.py        # State management
│   ├── tools/              # Tool implementations
│   │   ├── base.py         # Base tool interface
│   │   ├── web_search.py   # Web search tool
│   │   ├── database.py     # Database query tool
│   │   └── file_operations.py
│   ├── memory/             # Memory systems
│   │   ├── vector_memory.py    # Vector store
│   │   └── conversation_memory.py
│   ├── utils/              # Utilities
│   │   └── config.py       # Configuration
│   └── main.py             # CLI interface
├── tests/                  # Unit tests
├── data/                   # Data storage
├── logs/                   # Log files
├── config/                 # Configuration files
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── requirements.txt       # Python dependencies
└── .env.example          # Environment template
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4-turbo-preview
OPENAI_TEMPERATURE=0.0
MAX_TOKENS=4096

# Brave Search API
BRAVE_API_KEY=your_brave_api_key_here
BRAVE_SEARCH_LIMIT=5

# Database Configuration (optional)
DATABASE_URL=postgresql://user:password@localhost:5432/agentdb

# Agent Configuration
AGENT_MAX_ITERATIONS=10
AGENT_MAX_EXECUTION_TIME=300
AGENT_VERBOSE=true

# Memory Configuration
MEMORY_TYPE=chromadb
MEMORY_COLLECTION_NAME=agent_memory
MEMORY_PERSIST_DIRECTORY=./data/memory

# Cost Management
MAX_COST_PER_REQUEST=1.00
ENABLE_COST_TRACKING=true
```

## 💡 Usage Examples

### Interactive Mode

```bash
python -m src.main interactive
```

### Research Assistant

```bash
python -m src.main run "Research our top three competitors in the cloud database market. \
For each competitor, find their latest product announcements, pricing changes, and \
customer reviews from the past 30 days. Analyze trends and provide strategic recommendations."
```

### Data Analysis

```bash
python -m src.main run "Load the sales data from sales_q4_2024.csv, \
calculate month-over-month growth rates, identify the top 10 performing products, \
and create a summary report with insights."
```

### Customer Support Analysis

```bash
python -m src.main run "Analyze the latest 50 support tickets from the database, \
categorize them by issue type, identify recurring problems, \
and suggest process improvements."
```

## 🏗️ Architecture

### Agent Flow

```
User Input → Planner → Task Queue → Executor → Tools → Results → Reflector → Summary
```

### Tool Layer

Each tool implements a standardized interface:
- **Web Search Tool**: Query search engines and retrieve content
- **Database Tool**: Execute SQL queries (read-only for safety)
- **File Operations Tool**: Read/write CSV, JSON, text files

### Memory Layer

- **Short-term Memory**: In-memory conversation buffer
- **Long-term Memory**: Vector store with semantic search
- **Session Management**: Persistent context across interactions

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=html

# Run specific test file
pytest tests/test_tools.py -v
```

## 🐳 Docker Deployment

### Build and run with Docker Compose

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f agent

# Stop services
docker-compose down
```

### Build standalone Docker image

```bash
docker build -t enterprise-ai-agent .
docker run -it --env-file .env enterprise-ai-agent interactive
```

## 📊 Monitoring and Observability

### Structured Logging

All logs are written to:
- Console (INFO level)
- `logs/agent_{date}.log` (DEBUG level)
- `logs/errors_{date}.log` (ERROR level)

### Metrics

Prometheus-compatible metrics are collected:
- `agent_executions_total` - Total agent executions
- `agent_success_rate` - Success rate percentage
- `execution_duration_seconds` - Execution time histogram
- `tool_calls_total` - Tool usage by tool name and status

### Cost Tracking

Monitor LLM API costs:
```python
# View cost for last execution
agent.get_cost_metrics()

# Set budget limits in .env
MAX_COST_PER_REQUEST=1.00
```

## 🔒 Security Best Practices

### Implemented Security Controls

- ✅ Input validation with Pydantic models
- ✅ SQL injection prevention (read-only queries)
- ✅ Path traversal protection in file operations
- ✅ API key management via environment variables
- ✅ Rate limiting on external API calls
- ✅ Dangerous pattern detection in user inputs

### Security Checklist

Before deploying to production:
- [ ] Rotate all API keys
- [ ] Enable database connection encryption
- [ ] Configure firewall rules
- [ ] Set up API rate limiting
- [ ] Enable audit logging
- [ ] Implement user authentication
- [ ] Configure CORS policies
- [ ] Set resource limits in Docker

## 📈 Performance Optimization

### Best Practices

1. **Token Usage Optimization**
   - Cache LLM responses
   - Use shorter, focused prompts
   - Implement result summarization

2. **Parallel Execution**
   - Execute independent tasks concurrently
   - Use async/await for I/O operations
   - Implement connection pooling

3. **Memory Management**
   - Limit conversation history length
   - Implement memory cleanup routines
   - Use efficient vector stores

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**Issue: "OpenAI API key not configured"**
```bash
# Solution: Ensure .env file has valid API key
OPENAI_API_KEY=sk-...
```

**Issue: "Database connection failed"**
```bash
# Solution: Check DATABASE_URL format
DATABASE_URL=postgresql://user:password@host:port/database
```

**Issue: "Memory collection not found"**
```bash
# Solution: Memory directory is created automatically, but ensure permissions
mkdir -p data/memory
chmod 755 data/memory
```

## 📚 Additional Resources

### Documentation
- [LangChain Documentation](https://python.langchain.com)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [ChromaDB Documentation](https://docs.trychroma.com)

### Related Articles
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- [Building Production AI Systems - Best Practices](https://crashbytes.com)

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/CrashBytes/enterprise-ai-agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/CrashBytes/enterprise-ai-agent/discussions)
- **Blog**: [CrashBytes](https://crashbytes.com)

## 🌟 Acknowledgments

This project demonstrates enterprise-grade patterns for building production AI agents. Special thanks to:
- The LangChain community for excellent tooling
- Anthropic and OpenAI for advancing AI capabilities
- The open-source community for inspiration

---

**Built with ❤️ by [CrashBytes](https://crashbytes.com)**

**Tutorial**: [Building Production-Ready AI Agents](https://crashbytes.com/articles/building-production-ai-agents-multi-tool-langchain-openai-enterprise-automation-2025)
