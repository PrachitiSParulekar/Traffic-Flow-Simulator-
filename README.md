# Traffic Flow Simulator using Cellular Automata

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/matplotlib-%23ffffff.svg?style=flat&logo=matplotlib&logoColor=black)](https://matplotlib.org/)

Clean implementation of the **Nagel-Schreckenberg (NaSch)** cellular automaton model for traffic flow simulation with enhanced space-time visualization.

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/PrachitiSParulekar/Traffic-Flow-Simulator-.git
cd Traffic-Flow-Simulator-

# Install dependencies
pip install -r requirements.txt

# Run simulation
python traffic_simulator.py
```

## ✨ Features

- **Single-lane cellular automata** using Nagel-Schreckenberg model
- **Enhanced space-time diagrams** with speed-based color coding
- **Real-time traffic flow analysis** with statistical metrics
- **Fundamental diagram** showing flow-density relationship
- **70.4% flow efficiency** with realistic traffic patterns
- **Publication-ready visualizations** with high-resolution output

## 📸 Output

The simulator generates a comprehensive 4-panel analysis:
1. **Space-Time Diagram** - Vehicle positions and speeds over time
2. **Flow Analysis** - Traffic flow rate with statistical overlays  
3. **Speed Analysis** - Average speed tracking with efficiency metrics
4. **Fundamental Diagram** - Flow vs density relationship

## 🎯 Usage

```python
from traffic_simulator import TrafficSimulator

# Create and run simulation
simulator = TrafficSimulator(road_length=200, density=0.3, max_speed=5, brake_prob=0.2)
simulator.run_simulation(steps=300)
simulator.print_statistics()
simulator.create_enhanced_space_time_diagram()
```

## 🔬 Nagel-Schreckenberg Model

The simulation implements the classic NaSch cellular automaton rules:
1. **Acceleration**: `v → min(v+1, v_max)` if space allows
2. **Deceleration**: `v → min(v, gap)` to avoid collision  
3. **Random braking**: `v → max(v-1, 0)` with probability `p`
4. **Movement**: `x → (x + v) mod L` with periodic boundaries

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

⭐ **If you find this project useful, please give it a star!** ⭐
