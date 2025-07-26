#!/usr/bin/env python3
"""
Traffic Flow Simulator - Nagel-Schreckenberg Model
================================================

Clean implementation of cellular automata traffic simulation with enhanced visualization.

Author: Traffic Flow Analysis
Date: July 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

class TrafficSimulator:
    """Nagel-Schreckenberg traffic cellular automaton simulator."""
    
    def __init__(self, road_length=200, density=0.3, max_speed=5, brake_prob=0.2, random_seed=None):
        """Initialize traffic simulation.
        
        Parameters:
            road_length (int): Road length in cells
            density (float): Vehicle density [0.0, 1.0]
            max_speed (int): Maximum vehicle speed
            brake_prob (float): Random braking probability [0.0, 1.0]
            random_seed (int): Random seed for reproducibility
        """
        if random_seed:
            np.random.seed(random_seed)
            
        self.road_length = road_length
        self.max_speed = max_speed
        self.brake_prob = brake_prob
        self.density = density
        self.num_vehicles = int(density * road_length)
        
        # Initialize vehicles
        self.positions = np.sort(np.random.choice(road_length, self.num_vehicles, replace=False))
        self.speeds = np.random.randint(0, max_speed + 1, self.num_vehicles)
        
        # Data collection
        self.space_time_data = []
        self.flow_data = []
        self.avg_speed_data = []
        
    def get_road_state(self):
        """Return current road state array."""
        road = np.zeros(self.road_length)
        for i, pos in enumerate(self.positions):
            road[int(pos)] = self.speeds[i]
        return road
    
    def _calculate_gap(self, vehicle_pos):
        """Calculate gap to next vehicle with periodic boundaries."""
        next_vehicles = self.positions[self.positions > vehicle_pos]
        if len(next_vehicles) > 0:
            return next_vehicles[0] - vehicle_pos - 1
        
        # Handle wrap-around (periodic boundary)
        if len(self.positions[self.positions < vehicle_pos]) > 0:
            return (self.road_length - vehicle_pos - 1) + np.min(self.positions[self.positions < vehicle_pos])
        return self.road_length - 1
        
    def step(self):
        """Execute one simulation step using Nagel-Schreckenberg rules."""
        new_speeds = self.speeds.copy()
        new_positions = self.positions.copy()
        
        # Process vehicles in position order
        for idx in np.argsort(self.positions):
            pos = self.positions[idx]
            speed = self.speeds[idx]
            
            # 1. Acceleration
            if speed < self.max_speed:
                new_speeds[idx] = speed + 1
            
            # 2. Deceleration (collision avoidance)
            gap = self._calculate_gap(pos)
            if new_speeds[idx] > gap:
                new_speeds[idx] = max(0, int(gap))
            
            # 3. Random braking
            if new_speeds[idx] > 0 and np.random.random() < self.brake_prob:
                new_speeds[idx] = max(0, new_speeds[idx] - 1)
            
            # 4. Movement
            new_positions[idx] = (pos + new_speeds[idx]) % self.road_length
        
        # Update state
        self.speeds = new_speeds
        self.positions = new_positions
        
        # Collect data
        self._collect_data()
    
    def _collect_data(self):
        """Collect simulation data for analysis."""
        road_state = self.get_road_state()
        self.space_time_data.append(road_state)
        
        # Flow: total vehicle movement per time step
        flow = np.sum(self.speeds) / self.road_length
        self.flow_data.append(flow)
        
        # Average speed
        avg_speed = np.mean(self.speeds) if len(self.speeds) > 0 else 0
        self.avg_speed_data.append(avg_speed)
        
    def run_simulation(self, steps):
        """Run simulation for specified number of steps."""
        print(f"🚗 Running simulation: {steps} steps...")
        
        for step in range(steps):
            self.step()
            if (step + 1) % 50 == 0:
                print(f"   Step {step + 1}/{steps} completed")
        
        print("✓ Simulation completed!")
    
    def _create_colormap(self):
        """Create custom colormap for speed visualization."""
        colors = [
            '#000033',  # Empty (dark blue)
            '#000080',  # Speed 0 (blue)
            '#0040FF',  # Speed 1 (light blue)
            '#00BFFF',  # Speed 2 (cyan)
            '#40FF40',  # Speed 3 (green)
            '#FFFF00',  # Speed 4 (yellow)
            '#FF8000',  # Speed 5 (orange)
            '#FF0000'   # Speed 6+ (red)
        ]
        return mcolors.ListedColormap(colors[:self.max_speed + 2])
        
    def create_enhanced_space_time_diagram(self):
        """Create comprehensive traffic analysis visualization."""
        if not self.space_time_data:
            print("No simulation data available. Run simulation first.")
            return
            
        space_time_matrix = np.array(self.space_time_data)
        steps, road_length = space_time_matrix.shape
        
        # Create figure layout
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Traffic Flow Analysis - Nagel-Schreckenberg Model', 
                     fontsize=16, fontweight='bold')
        
        # 1. Space-Time Diagram
        self._plot_space_time_diagram(ax1, space_time_matrix, steps, road_length)
        
        # 2. Flow Rate Analysis
        self._plot_flow_analysis(ax2)
        
        # 3. Speed Analysis
        self._plot_speed_analysis(ax3)
        
        # 4. Fundamental Diagram
        self._plot_fundamental_diagram(ax4)
        
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"traffic_analysis_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✓ Visualization saved: {filename}")
        
        plt.show()
    
    def _plot_space_time_diagram(self, ax, space_time_matrix, steps, road_length):
        """Plot enhanced space-time diagram."""
        # Adjust matrix for visualization (shift speeds up by 1)
        vis_matrix = space_time_matrix.copy()
        vis_matrix[vis_matrix > 0] += 1
        
        custom_cmap = self._create_colormap()
        
        im = ax.imshow(vis_matrix, cmap=custom_cmap, aspect='auto', 
                      origin='lower', extent=[0, road_length, 0, steps],
                      interpolation='nearest')
        
        ax.set_title('Space-Time Diagram\n(Vehicle Positions & Speeds)', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Position (cells)', fontsize=12)
        ax.set_ylabel('Time (steps)', fontsize=12)
        ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
        
        # Colorbar
        cbar = plt.colorbar(im, ax=ax, shrink=0.8)
        cbar.set_label('Vehicle Speed', fontsize=11, fontweight='bold')
        cbar.set_ticks(range(self.max_speed + 2))
        cbar.set_ticklabels(['Empty'] + [str(i) for i in range(self.max_speed + 1)])
    
    def _plot_flow_analysis(self, ax):
        """Plot traffic flow rate over time."""
        ax.plot(self.flow_data, 'b-', linewidth=2, alpha=0.8, label='Flow Rate')
        ax.fill_between(range(len(self.flow_data)), self.flow_data, alpha=0.3, color='blue')
        
        avg_flow = np.mean(self.flow_data)
        ax.axhline(y=avg_flow, color='red', linestyle='--', alpha=0.7,
                  label=f'Average: {avg_flow:.3f}')
        
        ax.set_title('Traffic Flow Rate Over Time', fontsize=14, fontweight='bold')
        ax.set_xlabel('Time Step', fontsize=12)
        ax.set_ylabel('Flow Rate (vehicles/cell/step)', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
    
    def _plot_speed_analysis(self, ax):
        """Plot average speed over time."""
        ax.plot(self.avg_speed_data, 'g-', linewidth=2, alpha=0.8, label='Average Speed')
        ax.fill_between(range(len(self.avg_speed_data)), self.avg_speed_data, 
                       alpha=0.3, color='green')
        
        avg_speed = np.mean(self.avg_speed_data)
        ax.axhline(y=avg_speed, color='red', linestyle='--', alpha=0.7,
                  label=f'Overall Average: {avg_speed:.3f}')
        
        ax.set_title('Average Speed Over Time', fontsize=14, fontweight='bold')
        ax.set_xlabel('Time Step', fontsize=12)
        ax.set_ylabel('Average Speed (cells/step)', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
    
    def _plot_fundamental_diagram(self, ax):
        """Plot flow-density fundamental diagram."""
        local_densities = [self.density] * len(self.flow_data)
        
        scatter = ax.scatter(local_densities, self.flow_data, 
                           c=range(len(self.flow_data)), cmap='viridis', 
                           alpha=0.7, s=20)
        
        max_theoretical_flow = self.density * self.max_speed
        ax.axhline(y=max_theoretical_flow, color='red', linestyle='--', alpha=0.7,
                  label=f'Theoretical Max: {max_theoretical_flow:.3f}')
        
        ax.set_title('Fundamental Diagram\n(Flow vs Density)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Density', fontsize=12)
        ax.set_ylabel('Flow Rate', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
    def print_statistics(self):
        """Print comprehensive simulation statistics."""
        if not self.flow_data:
            print("No simulation data available.")
            return
            
        print("\n" + "="*60)
        print("📊 TRAFFIC SIMULATION ANALYSIS")
        print("="*60)
        
        # Simulation parameters
        print(f"Road Length:          {self.road_length} cells")
        print(f"Vehicles:             {self.num_vehicles}")
        print(f"Density:              {self.density:.1%}")
        print(f"Max Speed:            {self.max_speed} cells/step")
        print(f"Brake Probability:    {self.brake_prob:.1%}")
        print(f"Simulation Steps:     {len(self.flow_data)}")
        print("-" * 60)
        
        # Performance metrics
        avg_flow = np.mean(self.flow_data)
        avg_speed = np.mean(self.avg_speed_data)
        flow_std = np.std(self.flow_data)
        speed_std = np.std(self.avg_speed_data)
        
        flow_efficiency = avg_flow / (self.density * self.max_speed)
        speed_efficiency = avg_speed / self.max_speed
        
        print(f"Average Flow:         {avg_flow:.4f} ± {flow_std:.4f}")
        print(f"Average Speed:        {avg_speed:.4f} ± {speed_std:.4f}")
        print(f"Flow Efficiency:      {flow_efficiency:.1%}")
        print(f"Speed Efficiency:     {speed_efficiency:.1%}")
        print("="*60)


def main():
    """Main function to run traffic simulation analysis."""
    print("🚗 TRAFFIC FLOW SIMULATOR")
    print("Nagel-Schreckenberg Cellular Automaton")
    print("="*50)
    
    # Initialize and run simulation
    simulator = TrafficSimulator(
        road_length=200,
        density=0.3,
        max_speed=5,
        brake_prob=0.2,
        random_seed=42
    )
    
    simulator.run_simulation(steps=300)
    simulator.print_statistics()
    
    print("\n🎨 Creating visualization...")
    simulator.create_enhanced_space_time_diagram()
    
    print("\n🎉 Analysis complete!")
    return simulator


if __name__ == "__main__":
    main()
