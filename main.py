class RuleBasedSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []
    def add_rule(self, antecedent, consequent):
        self.rules.append((antecedent, consequent))
    def add_fact(self, fact):
        self.facts.add(fact)
    def forward_chain(self):
        new_fact_found = True
        while new_fact_found:
            new_fact_found = False
            for ante, cons in self.rules:
                if isinstance(ante, list):
                    condition_set = True
                    for condition in ante:
                        if isinstance(condition, list):
                            if "NOT" in condition:
                                for cond_not in condition:
                                    if cond_not in self.facts:
                                        condition_set = False
                            if "OR" in condition:
                                condition_set = False
                                for cond in condition:
                                    if cond in self.facts:
                                        condition_set = True
                                        break
                        elif not condition in self.facts:
                            condition_set = False
                else:
                    condition_set = ante in self.facts
                if condition_set and cons not in self.facts:
                    self.facts.add(cons)
                    new_fact_found = True
                    print(f'Inferred new fact: {cons}')
        print("\nInference complete. Final facts:")
        for fact in sorted(self.facts):
            print(f" - {fact}")

if __name__ == "__main__":
    system = RuleBasedSystem()

    system.add_rule("has_fur", "is_mammal")
    system.add_rule("has_feather", "is_bird")
    system.add_rule(["is_mammal", "eats_meat"], "is_carnivore")
    system.add_rule(["is_mammal", "has_hooves"], "is_ungulate")
    system.add_rule(["is_carnivore", "has_tawny_color", "has_dark_spots"], "is_cheetah")
    system.add_rule(["is_carnivore", "has_tawny_color", ["NOT", "has_dark_spots"]], "is_tiger")
    system.add_rule(["is_ungulate", "has_long_neck", "has_long_legs"], "is_giraffe")
    system.add_rule(["is_ungulate", "has_based_stripes"], "is_zebra")
    system.add_rule("is_bird", "is_animal")
    system.add_rule("is_mammal", "is_animal")

    system.add_fact("has_fur")
    system.add_fact("eats_meat")
    system.add_fact("has_tawny_color")
#    system.add_fact("has_dark_spots")
    system.add_fact("has_orange_color")


    system.forward_chain()
