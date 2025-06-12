# TFT Traits

A tool for exploring team compositions in Teamfight Tactics (TFT) Set 14, designed to find the best trait synergy combinations using greedy search algorithms.

## 🎯 Features

- **Intelligent Team Building**: Uses stochastic greedy search with epsilon-exploration to find optimal team compositions
- **Flexible Constraints**: Support for including/excluding specific champions and traits
- **Trait Prioritization**: Ability to prioritize certain traits with bonus scoring
- **Memory Optimized**: Efficient algorithm that maintains only top results during search
- **Comprehensive Analysis**: Detailed breakdown of trait synergies and activation levels
- **Customizable Scoring**: Scoring system that values trait levels exponentially

## 🚀 Quick Start

```python
from trait_optimizer_set_14 import TFTTraitOptimizer, champions_data, trait_thresholds

# Initialize the optimizer
optimizer = TFTTraitOptimizer(champions_data, trait_thresholds, epsilon=0.05)

# Find optimal 9-champion compositions
compositions = optimizer.find_optimal_combinations_greedy(
    team_size=9,
    top_n=5,
    num_epochs=1000,
    include_traits=["Street Demon", "Anima Squad"],  # Prioritize these traits
    exclude_traits=["Cypher"]  # Avoid this trait
)

# Analyze results
for i, comp in enumerate(compositions, 1):
    print(f"Composition {i} (Score: {comp['score']:.2f})")
    analysis = optimizer.analyze_composition(comp)
    print(f"Champions: {', '.join(analysis['champion_names'])}")
```

## 📋 Parameters

### `find_optimal_combinations_greedy()`

| Parameter | Type | Description |
|-----------|------|-------------|
| `team_size` | int | Size of the team (typically 8-10 for TFT) |
| `top_n` | int | Number of best compositions to return (default: 10) |
| `num_epochs` | int | Number of search iterations (default: 1000) |
| `include_champions` | list | Champions that must be included in the team |
| `exclude_champions` | list | Champions to exclude from consideration |
| `include_traits` | list | Traits to prioritize (get 2x value bonus) |
| `exclude_traits` | list | Traits to avoid completely |

## 🎮 TFT Set 14 Traits Supported

### Primary Traits (Origin)
- **Anima Squad** (3/5/7/10) - High scaling trait
- **BoomBots** (2/4/6) - Explosive synergy
- **Cyberboss** (2/4) - Elite units
- **Cypher** (3/4/5) - Stealth and precision
- **Divinicorp** (2/4/6) - Divine power
- **Exotech** (2/4/6) - Advanced technology
- **Golden Ox** (2/4/6) - Prosperity and strength
- **Nitro** (2/4/6) - Speed and energy
- **Street Demon** (3/5/7/10) - High scaling trait
- **Syndicate** (2/4/6) - Criminal organization

### Secondary Traits (Class)
- **A.M.P.** (3/5/7/10) - Amplified power
- **Bastion** (2/4/6) - Defensive fortress
- **Bruiser** (2/4/6) - Frontline fighters
- **Dynamo** (2/4/6) - Energy manipulation
- **Executioner** (2/4/6) - High damage dealers
- **Marksman** (2/4/6) - Ranged attackers
- **Rapidfire** (2/4/6) - Attack speed boost
- **Slayer** (2/4/6) - Assassin-type units
- **Strategist** (2/4/6) - Tactical support
- **Techie** (2/4/6) - Technology specialists
- **Vanguard** (2/4/6) - Tank units

### Unique Traits
- **Virus** (1) - Zac's unique trait
- **Soul Killer** (1) - Viego's unique trait
- **God of the Net** (1) - Garen's unique trait
- **Overlord** (1) - Renekton's unique trait

## 🧮 Scoring Algorithm

The optimizer uses a sophisticated scoring system:

1. **Base Trait Value**: `trait_level^2.5` (exponential scaling rewards higher trait levels)
2. **Prioritization Bonus**: 2x multiplier for traits in `include_traits`
3. **Diversity Bonus**: `√(active_traits)` rewards having multiple active traits
4. **Inclusion Bonus**: +5 points per active prioritized trait

## 💡 Usage Examples

### Basic Team Optimization
```python
# Find the best 8-champion team
compositions = optimizer.find_optimal_combinations_greedy(team_size=8, top_n=5)
```

### Build Around Specific Champions
```python
# Build a team that must include Jinx and Aphelios
compositions = optimizer.find_optimal_combinations_greedy(
    team_size=9,
    include_champions=["Jinx", "Aphelios"],
    top_n=5
)
```

### Prioritize Specific Traits
```python
# Focus on Street Demon and Marksman synergies
compositions = optimizer.find_optimal_combinations_greedy(
    team_size=9,
    include_traits=["Street Demon", "Marksman"],
    exclude_traits=["Cypher"],  # Avoid contested trait
    top_n=5
)
```

## 🔧 Algorithm Details

### Stochastic Greedy Search
- Uses epsilon-greedy exploration (default ε=0.05) to balance exploitation vs exploration
- Prioritizes champions with included traits during selection
- Memory-optimized to maintain only top-N results during search

### Trait Evaluation
- Considers trait thresholds and activation levels
- Applies exponential scaling to reward higher trait completions
- Ignores unique traits (Virus, Soul Killer, etc.) in base scoring

### Constraint Handling
- Validates all input parameters
- Ensures included champions exist in the dataset
- Maintains team size limits (TFT maximum: 10 units)

## 📊 Output Analysis

Each composition includes:
- **Score**: Numerical optimization score
- **Team Size**: Number of champions
- **Champions**: List of selected champions
- **Active Traits**: Trait levels and thresholds achieved
- **Prioritization Markers**: Shows which traits were prioritized

Example output:
```
--- Composition 1 (Score: 45.23) ---
Team Size: 9
Champions: Jinx, Brand, Ekko, Samira, Rengar, Aurora, Illaoi, Leona, Xayah
Active Traits:
  - Street Demon: 5/5 (Level 2) [PRIORITIZED]
  - Anima Squad: 5/5 (Level 2) [PRIORITIZED]
  - Marksman: 2/2 (Level 1)
  - Slayer: 2/2 (Level 1)
```

## 📝 Installation

1. Clone the repository:
```bash
git clone https://github.com/Mimsqueeze/tft-traits.git
```

2. Modify the `main()` function of `trait_optimizer_set_14.py` according to your specifications.

3. Run the optimizer:
```bash
python trait_optimizer_set_14.py
```

## ‼️ Note
Note, this is just a fun little project that is supposed to be proof-of-concept. I wanted to apply the concepts I learned in my Artificial Intelligence course, while also experimenting with using generative AI coding assistants like Claude, ChatGPT, and Github Copilot. I would NOT use the comps the program actually gives you lol.