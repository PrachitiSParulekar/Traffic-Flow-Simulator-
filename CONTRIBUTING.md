# Contributing to Traffic Flow Simulator

Thank you for your interest in contributing to the Traffic Flow Simulator project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues
- Use the GitHub issue tracker to report bugs
- Include Python version, OS, and error messages
- Provide steps to reproduce the issue

### Suggesting Features
- Open an issue with the "enhancement" label
- Describe the feature and its use case
- Include mockups or examples if applicable

### Code Contributions

#### Setup Development Environment
1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/traffic-flow-simulator.git`
3. Create virtual environment: `python -m venv venv`
4. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`

#### Making Changes
1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test your changes: `python traffic_simulator.py`
4. Commit with clear messages: `git commit -m "Add: description of changes"`
5. Push: `git push origin feature/your-feature-name`
6. Create a Pull Request

#### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for new functions and classes
- Keep functions focused and concise
- Add comments for complex logic

#### Testing
- Test your changes thoroughly
- Ensure the simulation runs without errors
- Verify visualizations are generated correctly
- Check that statistics are calculated properly

## Development Guidelines

### Code Organization
- Keep the main `TrafficSimulator` class clean and focused
- Use private methods (prefix with `_`) for internal functionality
- Separate visualization logic into dedicated methods
- Follow the existing code structure

### Documentation
- Update README.md if adding new features
- Add docstrings for new methods
- Include parameter descriptions and types
- Provide usage examples for complex features

### Performance
- Consider computational efficiency for large simulations
- Use NumPy operations where possible
- Profile code changes if modifying core algorithms

## Questions?

Feel free to open an issue for any questions about contributing!
