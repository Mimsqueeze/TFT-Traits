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
    "Cyberboss": [2, 3, 4, None],
    "Cypher": [3, 4, 5, None],
    "Divinicorp": [2, 4, 6, None],
    "Exotech": [3, 5, 7, 10],
    "Golden Ox": [2, 4, 6, None],
    "Nitro": [3, None, 4, None],
    "Syndicate": [3, 5, 7, None],
    "Street Demon": [3, 5, 7, 10],
    "A.M.P.": [2, 3, 5, None],
    "Bastion": [2, 4, 6, None],
    "Bruiser": [2, 4, 6, None],
    "Dynamo": [2, 3, 4, None],
    "Executioner": [2, 3, 5, None],
    "Marksman": [2, 4, None, None],
    "Rapidfire": [2, 4, 6, None],
    "Slayer": [2, 4, None, None],
    "Strategist": [2, 4, None, None],
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
    
    def calculate_trait_value(self, trait_name, count, exclude_traits=None, include_traits=None):
        """Calculate the value of a trait based on its count and thresholds."""
        
        # Check if trait is excluded
        if exclude_traits and trait_name in exclude_traits:
            return 0

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
        
        base_value = trait_level ** 2.5
        
        # Apply bonus for included traits
        if include_traits and trait_name in include_traits:
            base_value *= 2.0  # Double the value for prioritized traits
        
        return base_value
    
    def evaluate_team_composition(self, champions, exclude_traits=None, include_traits=None):
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
        included_traits_present = 0
        
        for trait, count in trait_counts.items():
            trait_value = self.calculate_trait_value(trait, count, exclude_traits, include_traits)
            if trait_value > 0:
                total_value += trait_value
                active_traits += 1
                
                # Track if we have any of the included traits active
                if include_traits and trait in include_traits:
                    included_traits_present += 1
        
        # Bonus for having multiple active traits (diversity bonus)
        diversity_bonus = math.sqrt(active_traits)
        
        # Additional bonus for including prioritized traits
        inclusion_bonus = 0
        if include_traits and included_traits_present > 0:
            inclusion_bonus = included_traits_present * 5  # Bonus for each included trait that's active
        
        return total_value + diversity_bonus + inclusion_bonus
    
    def _get_champion_by_name(self, name):
        """Get champion object by name."""
        for champion in self.champions:
            if champion['name'] == name:
                return champion
        return None
    
    def _filter_champions(self, include_champions=None, exclude_champions=None):
        """Filter champions based on include/exclude lists."""
        available_champions = self.champions.copy()
        
        # If include_champions is specified, start with only those champions
        if include_champions:
            included_champs = []
            for name in include_champions:
                champ = self._get_champion_by_name(name)
                if champ:
                    included_champs.append(champ)
            # Add remaining champions not in the include list
            for champ in self.champions:
                if champ['name'] not in include_champions:
                    included_champs.append(champ)
            available_champions = included_champs
        
        # Remove excluded champions
        if exclude_champions:
            available_champions = [
                champ for champ in available_champions 
                if champ['name'] not in exclude_champions
            ]
        
        return available_champions
    
    def _champion_has_included_traits(self, champion, include_traits):
        """Check if a champion has any of the included traits."""
        if not include_traits:
            return False
        return any(trait in include_traits for trait in champion['traits'])
    
    def find_optimal_combinations_greedy(self, team_size, top_n=10, num_epochs=1000, 
                                       include_champions=None, exclude_champions=None, 
                                       exclude_traits=None, include_traits=None):
        """Find optimal trait combinations using a greedy approach with constraints."""
        
        # Validate include_champions
        if include_champions:
            if len(include_champions) > team_size:
                raise ValueError(f"Cannot include {len(include_champions)} champions in a team of size {team_size}")
            
            # Check that all included champions exist
            for name in include_champions:
                if not self._get_champion_by_name(name):
                    raise ValueError(f"Champion '{name}' not found in champion data")
        
        # Validate include_traits
        if include_traits:
            for trait in include_traits:
                if trait not in self.trait_thresholds:
                    raise ValueError(f"Trait '{trait}' not found in trait data")
        
        best_combinations = []
        
        # Run num_epochs stochastic greedy searches
        for _ in range(num_epochs):
            result = self.stochastic_greedy_search(
                team_size, include_champions, exclude_champions, exclude_traits, include_traits
            )
            if result:
                # Memory-optimized: only keep top_n results
                if len(best_combinations) < top_n:
                    best_combinations.append(result)
                else:
                    # Find the worst score in current best_combinations
                    min_score = min(best_combinations, key=lambda x: x['score'])['score']
                    if result['score'] > min_score:
                        # Remove the worst and add the new result
                        best_combinations = [comp for comp in best_combinations if comp['score'] != min_score]
                        best_combinations.append(result)
        
        # Sort by score and return results
        best_combinations.sort(key=lambda x: x['score'], reverse=True)
        return best_combinations
    
    def stochastic_greedy_search(self, team_size, include_champions=None, 
                               exclude_champions=None, exclude_traits=None, include_traits=None):
        """Greedy search for best team of given size with constraints."""
        current_team = []
        
        # Start with required champions
        if include_champions:
            for name in include_champions:
                champ = self._get_champion_by_name(name)
                if champ:
                    current_team.append(champ)
        
        # Get remaining available champions
        remaining_champions = self._filter_champions(include_champions, exclude_champions)
        
        # Remove already included champions from remaining pool
        remaining_champions = [
            champ for champ in remaining_champions 
            if champ not in current_team
        ]
        
        # If we already have enough champions from the include list, return early
        if len(current_team) >= team_size:
            return {
                'team': current_team[:team_size],
                'score': self.evaluate_team_composition(current_team[:team_size], exclude_traits, include_traits),
                'size': min(len(current_team), team_size)
            }
        
        # If we don't have any included champions, prioritize champions with included traits
        if len(current_team) == 0 and remaining_champions:
            if include_traits:
                # Try to find a champion with included traits first
                champions_with_traits = [
                    champ for champ in remaining_champions 
                    if self._champion_has_included_traits(champ, include_traits)
                ]
                if champions_with_traits:
                    first_champion = random.choice(champions_with_traits)
                else:
                    first_champion = random.choice(remaining_champions)
            else:
                first_champion = random.choice(remaining_champions)
            
            current_team.append(first_champion)
            remaining_champions.remove(first_champion)

        # Fill remaining slots
        slots_to_fill = team_size - len(current_team)
        for _ in range(slots_to_fill):
            if not remaining_champions:
                break
                
            # epsilon probability of exploring, but bias towards champions with included traits
            if random.random() < self.epsilon:
                if include_traits:
                    # 70% chance to pick from champions with included traits if available
                    champions_with_traits = [
                        champ for champ in remaining_champions 
                        if self._champion_has_included_traits(champ, include_traits)
                    ]
                    if champions_with_traits and random.random() < 0.7:
                        random_champion = random.choice(champions_with_traits)
                    else:
                        random_champion = random.choice(remaining_champions)
                else:
                    random_champion = random.choice(remaining_champions)
                
                current_team.append(random_champion)
                remaining_champions.remove(random_champion)
                continue

            best_champion = None
            best_score = -float('inf')
            
            for champion in remaining_champions:
                test_team = current_team + [champion]
                score = self.evaluate_team_composition(test_team, exclude_traits, include_traits)
                
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
                'score': self.evaluate_team_composition(current_team, exclude_traits, include_traits),
                'size': len(current_team)
            }
        return None
    
    def analyze_composition(self, composition, exclude_traits=None, include_traits=None):
        """Analyze a team composition and return detailed breakdown."""
        trait_counts = Counter()
        for champion in composition['team']:
            for trait in champion['traits']:
                trait_counts[trait] += 1
        
        active_traits = {}
        for trait, count in trait_counts.items():
            # Skip excluded traits in analysis display
            if exclude_traits and trait in exclude_traits:
                continue
                
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
                is_included = include_traits and trait in include_traits
                active_traits[trait] = {
                    'count': count,
                    'level': active_level,
                    'threshold': thresholds[active_level - 1],
                    'is_prioritized': is_included
                }
        
        return {
            'composition': composition,
            'trait_counts': dict(trait_counts),
            'active_traits': active_traits,
            'champion_names': [champ['name'] for champ in composition['team']]
        }

def main():
    # Initialize optimizer
    optimizer = TFTTraitOptimizer(champions_data, trait_thresholds, epsilon=0.2)
    # Note, when prioritizing traits, higher epsilon leads to more vertical builds, while lower epsilon leads to more horizontal builds

    
    print("TFT Set 14 Trait Combination Optimizer")
    print("=" * 50)
    
    constrained_comps = optimizer.find_optimal_combinations_greedy(
        team_size=9, 
        top_n=5, 
        num_epochs=10000,
        include_champions=["Aurora"],
        exclude_champions=[],
        exclude_traits=["Cypher"],
        include_traits=[]  # Example: prioritize these traits
    )
    
    for i, comp in enumerate(constrained_comps, 1):
        print(f"\n--- Constrained Composition {i} (Score: {comp['score']:.2f}) ---")
        analysis = optimizer.analyze_composition(comp, exclude_traits=["Cypher"], include_traits=[])
        
        print(f"Team Size: {comp['size']}")
        print(f"Champions: {', '.join(analysis['champion_names'])}")
        print("Active Traits:")
        for trait, info in analysis['active_traits'].items():
            priority_marker = " [PRIORITIZED]" if info['is_prioritized'] else ""
            print(f"  - {trait}: {info['count']}/{info['threshold']} (Level {info['level']}){priority_marker}")

if __name__ == "__main__":
    main()