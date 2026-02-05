# Contributing to Akira99

## Development Setup

```bash
git clone https://github.com/myAkira99/Akira99.git
cd Akira99
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing

```bash
pytest tests/ -v --cov=akira99
```

## Commit Format

```
feat(module): description
fix(module): description
test(module): description
docs: description
chore: description
```

Include co-author: `Co-Authored-By: Name <email@example.com>`
