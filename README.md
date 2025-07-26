# Traffic Flow Simulator using Cellular Automata

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)](https://matplotlib.org/)

Clean implementation of the **Nagel-Schreckenberg (NaSch)** cellular automaton model for traffic flow simulation with enhanced space-time visualization.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run simulation
python traffic_simulator.py
```

## ✨ Features

### 🚗 **Traffic Simulation**
- **Single-lane cellular automata** using Nagel-Schreckenberg model
- **Realistic traffic dynamics** with acceleration, deceleration, and random braking
- **Configurable parameters** (road length, density, max speed, brake probability)
- **Periodic boundary conditions** for continuous traffic flow

### 📊 **Enhanced Visualization**
- **High-quality space-time diagrams** with speed-based color coding
- **Real-time traffic flow analysis** with flow rate and average speed tracking
- **Fundamental diagram** showing flow-density relationship
- **Statistical analysis** with efficiency metrics and variability measures
- **Clean, publication-ready plots** with professional styling

### 🎯 **Core Features**
- Clean, standalone Python implementation
- Minimal dependencies (NumPy, Matplotlib)
- Easy-to-understand code structure
- Comprehensive traffic statistics
- High-resolution visualization output

## 📸 Example Output

The simulator generates a comprehensive 4-panel analysis:

1. **Space-Time Diagram**: Vehicle positions and speeds over time
2. **Flow Analysis**: Traffic flow rate with statistical overlays  
3. **Speed Analysis**: Average speed tracking with efficiency metrics
4. **Fundamental Diagram**: Flow vs density relationship

*Sample visualization showing 70.4% flow efficiency with realistic traffic patterns.*

## Project Structure

```
traffic-flow-simulator/
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI/CD
├── traffic_simulator.py           # **MAIN SIMULATOR** (Complete solution)
├── requirements.txt               # Python dependencies
├── README.md                      # This documentation
├── LICENSE                        # MIT License
├── CONTRIBUTING.md                # Contribution guidelines
├── CHANGELOG.md                   # Version history
├── .gitignore                     # Git ignore patterns
└── traffic_analysis_*.png         # Generated visualizations
```

## 🎯 Usage

### Run the Simulator
```bash
python traffic_simulator.py
```

### Programmatic Usage
```python
from traffic_simulator import TrafficSimulator

# Create simulator with custom parameters
simulator = TrafficSimulator(
    road_length=200,    # Road length in cells
    density=0.3,        # Vehicle density (30%)
    max_speed=5,        # Maximum speed
    brake_prob=0.2,     # Random braking probability (20%)
    random_seed=42      # For reproducible results
)

# Run simulation
simulator.run_simulation(steps=300)

# Display statistics
simulator.print_statistics()

# Generate visualizations
simulator.create_enhanced_space_time_diagram()
```

## 🛠️ Installation

### Requirements
- **Python 3.7+**
- **NumPy** - Numerical computations
- **Matplotlib** - Visualization and plotting
- **SciPy** - Scientific computing (optional)
- **Pandas** - Data analysis (optional)

### Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/PrachitiSParulekar/Traffic-Flow-Simulator-.git
   cd Traffic-Flow-Simulator-
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the simulation**:
   ```bash
   python traffic_simulator.py
   ```

That's it! The simulator will run and generate beautiful visualizations automatically.

## Dependencies

- **Python 3.7+**
- **NumPy** - Numerical computations
- **Matplotlib** - Visualization and plotting
- **SciPy** - Scientific computing (for advanced features)
- **Pandas** - Data analysis (for advanced features)

## Simulation Parameters

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| `road_length` | Number of cells in road | 200 | 50-1000 |
| `density` | Vehicle density ratio | 0.3 | 0.1-0.8 |
| `max_speed` | Maximum vehicle speed | 5 | 1-10 |
| `brake_prob` | Random braking probability | 0.2 | 0.0-1.0 |
| `steps` | Simulation time steps | 300 | 100-2000 |

## Output

The simulator generates:
- **Space-time diagram** showing vehicle positions and speeds over time
- **Flow rate analysis** with time series plots
- **Average speed tracking** throughout simulation
- **Fundamental diagram** illustrating flow-density relationship
- **Statistical summary** with efficiency metrics
- **High-resolution PNG files** for publication/presentation

## Understanding the Visualization

### Space-Time Diagram
- **X-axis**: Road position (cells)
- **Y-axis**: Time (simulation steps)
- **Colors**: Vehicle speeds (dark blue = empty, red = highest speed)
- **Patterns**: Traffic waves, congestion, and free flow regions

### Traffic Metrics
- **Flow Rate**: Vehicles passing per cell per time step
- **Flow Efficiency**: Actual flow / theoretical maximum flow
- **Speed Efficiency**: Average speed / maximum possible speed
- **Variability**: Standard deviation indicating traffic stability

## 🔬 Nagel-Schreckenberg Model

The simulation implements the classic NaSch cellular automaton rules:

1. **Acceleration**: `v → min(v+1, v_max)` if space allows
2. **Deceleration**: `v → min(v, gap)` to avoid collision  
3. **Random braking**: `v → max(v-1, 0)` with probability `p`
4. **Movement**: `x → (x + v) mod L` with periodic boundaries

### Model Features
- **Discrete time steps** for computational efficiency
- **Periodic boundary conditions** simulating infinite highway
- **Stochastic braking** introducing realistic traffic variations
- **Gap-dependent deceleration** preventing collisions

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Educational Use

This simulator is perfect for:
- **Traffic engineering courses** - Understanding traffic flow dynamics
- **Physics simulations** - Studying collective behavior and phase transitions
- **Computer science** - Learning cellular automata and simulation techniques
- **Research** - Investigating traffic phenomena and optimization strategies

## 📚 References

- Nagel, K., & Schreckenberg, M. (1992). A cellular automaton model for freeway traffic. *Journal de physique I*, 2(12), 2221-2229.
- Chowdhury, D., Santen, L., & Schadschneider, A. (2000). Statistical physics of vehicular traffic and some related systems. *Physics Reports*, 329(4-6), 199-329.

## 🔗 Related Projects

- [SUMO](https://eclipse.org/sumo/) - Simulation of Urban MObility
- [TraCI](https://sumo.dlr.de/docs/TraCI.html) - Traffic Control Interface
- [CellularAutomata.jl](https://github.com/natevmp/CellularAutomata.jl) - Julia implementation

---

⭐ **If you find this project useful, please give it a star!** ⭐

**Repository**: [https://github.com/PrachitiSParulekar/Traffic-Flow-Simulator-](https://github.com/PrachitiSParulekar/Traffic-Flow-Simulator-)
