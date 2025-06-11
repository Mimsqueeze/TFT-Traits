from itertools import combinations
from collections import defaultdict, Counter
import math
import random

# Champions data
champions_data = [
    {"name": "Alistar", "traits": ["Golden Ox", "Bruiser"]},
    {"name": "Annie", "traits": ["Golden Ox", "A.M.P."]},
    {"name": "Aphelios", "traits": ["Golden Ox", "Marksman"]},
    {"name": "Aurora", "traits": ["Anima Squad", "Dynamo"]},
    {"name": "Brand", "traits": ["Street Demon", "Techie"]},
    {"name": "Braum", "traits": ["Syndicate", "Vanguard"]},
    {"name": "Cho'Gath", "traits": ["BoomBots", "Bruiser"]},
    {"name": "Darius", "traits": ["Syndicate", "Bruiser"]},
    {"name": "Draven", "traits": ["Cypher", "Rapidfire"]},
    {"name": "Dr.Mundo", "traits": ["Street Demon", "Bruiser", "Slayer"]},
    {"name": "Ekko", "traits": ["Street Demon", "Strategist"]},
    {"name": "Elise", "traits": ["Nitro", "Dynamo"]},
    {"name": "Fiddlesticks", "traits": ["BoomBots", "Techie"]},
    {"name": "Galio", "traits": ["Cypher", "Bastion"]},
    {"name": "Garen", "traits": ["God of the Net"]},
    {"name": "Gragas", "traits": ["Divinicorp", "Bruiser"]},
    {"name": "Graves", "traits": ["Golden Ox", "Executioner"]},
    {"name": "Illaoi", "traits": ["Anima Squad", "Bastion"]},
    {"name": "Jarvan IV", "traits": ["Golden Ox", "Vanguard", "Slayer"]},
    {"name": "Jax", "traits": ["Exotech", "Bastion"]},
    {"name": "Jhin", "traits": ["Exotech", "Marksman", "Dynamo"]},
    {"name": "Jinx", "traits": ["Street Demon", "Marksman"]},
    {"name": "Kindred", "traits": ["Nitro", "Rapidfire", "Marksman"]},
    {"name": "Kobuko", "traits": ["Cyberboss", "Bruiser"]},
    {"name": "Kog'Maw", "traits": ["BoomBots", "Rapidfire"]},
    {"name": "LeBlanc", "traits": ["Cypher", "Strategist"]},
    {"name": "Leona", "traits": ["Anima Squad", "Vanguard"]},
    {"name": "Miss Fortune", "traits": ["Syndicate", "Dynamo"]},
    {"name": "Mordekaiser", "traits": ["Exotech", "Bruiser", "Techie"]},
    {"name": "Morgana", "traits": ["Divinicorp", "Dynamo"]},
    {"name": "Naafiri", "traits": ["Exotech", "A.M.P."]},
    {"name": "Neeko", "traits": ["Street Demon", "Strategist"]},
    {"name": "Nidalee", "traits": ["Nitro", "A.M.P."]},
    {"name": "Poppy", "traits": ["Cyberboss", "Bastion"]},
    {"name": "Renekton", "traits": ["Overlord", "Divinicorp", "Bastion"]},
    {"name": "Rengar", "traits": ["Street Demon", "Executioner"]},
    {"name": "Rhaast", "traits": ["Divinicorp", "Vanguard"]},
    {"name": "Samira", "traits": ["Street Demon", "A.M.P."]},
    {"name": "Sejuani", "traits": ["Exotech", "Bastion"]},
    {"name": "Senna", "traits": ["Divinicorp", "Slayer"]},
    {"name": "Seraphine", "traits": ["Anima Squad", "Techie"]},
    {"name": "Shaco", "traits": ["Syndicate", "Slayer"]},
    {"name": "Shyvana", "traits": ["Nitro", "Bastion", "Techie"]},
    {"name": "Skarner", "traits": ["BoomBots", "Vanguard"]},
    {"name": "Sylas", "traits": ["Anima Squad", "Vanguard"]},
    {"name": "Twisted Fate", "traits": ["Syndicate", "Rapidfire"]},
    {"name": "Urgot", "traits": ["BoomBots", "Executioner"]},
    {"name": "Varus", "traits": ["Exotech", "Executioner"]},
    {"name": "Vayne", "traits": ["Anima Squad", "Slayer"]},
    {"name": "Veigar", "traits": ["Cyberboss", "Techie"]},
    {"name": "Vex", "traits": ["Divinicorp", "Executioner"]},
    {"name": "Vi", "traits": ["Cypher", "Vanguard"]},
    {"name": "Viego", "traits": ["Soul Killer", "Golden Ox", "Techie"]},
    {"name": "Xayah", "traits": ["Anima Squad", "Marksman"]},
    {"name": "Yuumi", "traits": ["Anima Squad", "A.M.P.", "Strategist"]},
    {"name": "Zac", "traits": ["Virus"]},
    {"name": "Zed", "traits": ["Cypher", "Slayer"]},
    {"name": "Zeri", "traits": ["Exotech", "Rapidfire"]},
    {"name": "Ziggs", "traits": ["Cyberboss", "Strategist"]},
    {"name": "Zyra", "traits": ["Street Demon", "Techie"]}
]

# Trait thresholds data
trait_thresholds = {
    "Anima Squad": [3, 5, 7, 10],
    "BoomBots": [2, 4, 6, None],
    "Cyberboss": [2, 4, None, None],
    "Cypher": [3, 4, 5, None],
    "Divinicorp": [2, 4, 6, None],
    "Exotech": [2, 4, 6, None],
    "Golden Ox": [2, 4, 6, None],
    "Nitro": [2, 4, 6, None],
    "Syndicate": [2, 4, 6, None],
    "Street Demon": [3, 5, 7, 10],
    "A.M.P.": [3, 5, 7, 10],
    "Bastion": [2, 4, 6, None],
    "Bruiser": [2, 4, 6, None],
    "Dynamo": [2, 4, 6, None],
    "Executioner": [2, 4, 6, None],
    "Marksman": [2, 4, 6, None],
    "Rapidfire": [2, 4, 6, None],
    "Slayer": [2, 4, 6, None],
    "Strategist": [2, 4, 6, None],
    "Techie": [2, 4, 6, None],
    "Vanguard": [2, 4, 6, None],
    "Virus": [1, None, None, None],
    "Soul Killer": [1, None, None, None],
    "God of the Net": [1, None, None, None],
    "Overlord": [1, None, None, None]
}

class TFTTraitOptimizer:
    def __init__(self, champions_data, trait_thresholds, epsilon):
        self.champions = champions_data
        self.trait_thresholds = trait_thresholds
        self.trait_to_champions = self._build_trait_mapping()
        self.epsilon = epsilon
    
    def _build_trait_mapping(self):
        """Build a mapping from traits to champions that have them."""
        trait_map = defaultdict(list)
        for champion in self.champions:
            for trait in champion['traits']:
                trait_map[trait].append(champion['name'])
        return trait_map
    
    def calculate_trait_value(self, trait_name, count):
        """Calculate the value of a trait based on its count and thresholds."""

        # Don't count singleton traits
        if trait_name in ["Virus", "Soul Killer", "God of the Net", "Overlord"]:
            return 0

        thresholds = self.trait_thresholds.get(trait_name, [])
        if not thresholds:
            return 0
        
        # Find the highest threshold reached
        trait_level = 0
        for i, threshold in enumerate(thresholds):
            if threshold is None:
                break
            if count >= threshold:
                trait_level = i + 1
            else:
                break
        
        # Scoring system: Higher trait levels are exponentially more valuable
        if trait_level == 0:
            return 0
        
        base_value = trait_level ** 2
        return base_value
    
    def evaluate_team_composition(self, champions):
        """Evaluate a team composition based on trait synergies."""
        if len(champions) > 10:  # TFT team size limit
            return 0
        
        # Count traits
        trait_counts = Counter()
        for champion in champions:
            for trait in champion['traits']:
                trait_counts[trait] += 1
        
        # Calculate total value
        total_value = 0
        active_traits = 0
        
        for trait, count in trait_counts.items():
            trait_value = self.calculate_trait_value(trait, count)
            if trait_value > 0:
                total_value += trait_value
                active_traits += 1
        
        # Bonus for having multiple active traits (diversity bonus)
        diversity_bonus = math.sqrt(active_traits)
        
        return total_value + diversity_bonus
    
    def find_optimal_combinations_greedy(self, team_size, top_n=10, num_epochs=1000):
        """Find optimal trait combinations using a greedy approach."""
        best_combinations = []
        
        # Run num_epochs stochastic greedy searches
        for _ in range(num_epochs):
            best_combinations.append(self.stochastic_greedy_search(team_size))
        
        # Sort by score and return top N
        best_combinations.sort(key=lambda x: x['score'], reverse=True)
        return best_combinations[:top_n]
    
    def stochastic_greedy_search(self, team_size):
        """Greedy search for best team of given size."""
        current_team = []
        remaining_champions = self.champions.copy()
        
        # Randomly choose the first champion for more variety
        first_champion = random.choice(remaining_champions)
        current_team.append(first_champion)
        remaining_champions.remove(first_champion)

        for _ in range(team_size-1):

            # epsilon probability of exploring
            if random.random() < self.epsilon:
                random_champion = random.choice(remaining_champions)
                current_team.append(random_champion)
                remaining_champions.remove(random_champion)
                continue

            best_champion = None
            best_score = -float('inf')
            
            for champion in remaining_champions:
                test_team = current_team + [champion]
                score = self.evaluate_team_composition(test_team)
                
                if score > best_score:
                    best_score = score
                    best_champion = champion
            
            if best_champion:
                current_team.append(best_champion)
                remaining_champions.remove(best_champion)
            else:
                break
        
        if current_team:
            return {
                'team': current_team,
                'score': self.evaluate_team_composition(current_team),
                'size': len(current_team)
            }
        return None
    
    def analyze_composition(self, composition):
        """Analyze a team composition and return detailed breakdown."""
        trait_counts = Counter()
        for champion in composition['team']:
            for trait in champion['traits']:
                trait_counts[trait] += 1
        
        active_traits = {}
        for trait, count in trait_counts.items():
            thresholds = self.trait_thresholds[trait]
            active_level = 0
            
            for i, threshold in enumerate(thresholds):
                if threshold is None:
                    break
                if count >= threshold:
                    active_level = i + 1
                else:
                    break
            
            if active_level > 0:
                active_traits[trait] = {
                    'count': count,
                    'level': active_level,
                    'threshold': thresholds[active_level - 1]
                }
        
        return {
            'composition': composition,
            'trait_counts': dict(trait_counts),
            'active_traits': active_traits,
            'champion_names': [champ['name'] for champ in composition['team']]
        }

def main():
    # Initialize optimizer
    optimizer = TFTTraitOptimizer(champions_data, trait_thresholds, epsilon=0.05)
    
    print("TFT Set 14 Trait Combination Optimizer")
    print("=" * 50)
    
    # Find optimal combinations
    print("\n1. Finding optimal team compositions...")
    optimal_comps = optimizer.find_optimal_combinations_greedy(team_size=8, top_n=10, num_epochs=1000)
    
    for i, comp in enumerate(optimal_comps, 1):
        print(f"\n--- Top {i} Composition (Score: {comp['score']:.2f}) ---")
        analysis = optimizer.analyze_composition(comp)
        
        print(f"Team Size: {comp['size']}")
        print(f"Champions: {', '.join(analysis['champion_names'])}")
        print("Active Traits:")
        for trait, info in analysis['active_traits'].items():
            print(f"  - {trait}: {info['count']}/{info['threshold']} (Level {info['level']})")

if __name__ == "__main__":
    main()