from pathlib import Path
from typing import List

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()

BOSS_HIT = 51
BOSS_DAMAGE = 9


SPELL_COSTS = {
    'magic_missle': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229,
}
from collections import namedtuple
SpellEffect = namedtuple('SpellEffect', ['name', 'cost', 'dmg', 'heal', 'mana', 'armor', 'num_turns' ])


spells = []
mm = SpellEffect(name='magic_missile', cost=53, dmg=4, heal=0, mana=0, armor=0, num_turns=0)
drain = SpellEffect(name='drain', cost=73, dmg=2, heal=2, mana=0, armor=0, num_turns=0)
shield = SpellEffect(name='shield', cost=113, dmg=0, heal=0, mana=0, armor=7, num_turns=6)
poison = SpellEffect(name='poison', cost=173, dmg=3, heal=0, mana=0, armor=0, num_turns=6)
recharge = SpellEffect(name='recharge', cost=229, dmg=0, heal=0, mana=101, armor=0, num_turns=5)

spells.append(mm)
spells.append(drain)
spells.append(shield)
spells.append(poison)
spells.append(recharge)

PLAYER_HIT = 50
PLAYER_MANA = 500

GameState = namedtuple('GameState', ['active_effects', 'boss_hit', 'player_hit', 'player_mana', 'mana_spent', 'spell', 'spellhistory'])




def play_turn(game_state: GameState):
    print("Starting spell history")
    print(game_state.spellhistory)
    print("Mana spent")
    print(game_state.mana_spent)
    active_effects = game_state.active_effects
    boss_hit = game_state.boss_hit
    player_hit= game_state.player_hit
    player_mana=game_state.player_mana
    spell_effect = game_state.spell
    player_armor = 0
    print("--Before Turn Lose 1 health")
    player_hit -= 1
    if player_hit <=0:
        print("Player looses")
        return GameState(active_effects, boss_hit, player_hit, player_mana, mana_spent=game_state.mana_spent, spell=None, spellhistory=game_state.spellhistory)
    print("---Player Turn---")
    print(f"- Player has {player_hit} hit points, {player_armor} armor, {player_mana} mana")
    print(f"- Boss has {boss_hit} hit points")
    print(f"Checking active effects : count {len(active_effects)}")
    for eff in active_effects:
        if eff.dmg > 0:
            boss_hit -= eff.dmg
            print(f"{eff.name} deals {eff.dmg} damage; its timer is now {eff.num_turns-1}")
        if eff.heal > 0:
            player_hit += eff.heal
            print(f"{eff.name} heals {eff.heal} health; its timer is now {eff.num_turns-1}")
        if eff.armor> 0:
            player_armor = eff.armor
            print(f"{eff.name} gives {eff.armor} armor; its timer is now {eff.num_turns-1}")
        if eff.mana > 0:
            player_mana += eff.mana
            print(f"{eff.name} gives {eff.mana} mana; its timer is now {eff.num_turns-1}")

    active_effects = [i._replace(num_turns=i.num_turns-1) for i in active_effects]
    active_effects = [i for i in active_effects if i.num_turns > 0]
    if boss_hit <= 0:
        print("Player wins")
        return GameState(active_effects, boss_hit, player_hit, player_mana, mana_spent=game_state.mana_spent, spell=None, spellhistory=game_state.spellhistory)
    if spell_effect.num_turns > 0:
        print(f"Player casts {spell_effect.name}")
        active_effects.append(spell_effect)
    else:
        if spell_effect.name == "magic_missile":
            print(f"Player casts {spell_effect.name} dealing {spell_effect.dmg} for {spell_effect.cost} mana")
            boss_hit -= spell_effect.dmg
        elif spell_effect.name == "drain":
            print(f"Player casts {spell_effect.name} dealing {spell_effect.dmg} and healing {spell_effect.heal} health for {spell_effect.cost} mana")
            boss_hit -= spell_effect.dmg
            player_hit += spell_effect.heal

    if boss_hit <= 0:
        print("Player wins")
        return GameState(active_effects, boss_hit, player_hit, player_mana, mana_spent=game_state.mana_spent, spell=None, spellhistory=game_state.spellhistory)

    print("---BOSS Turn---")
    print("--Before Turn Lose 1 health")
    # player_hit -= 1
    # if player_hit <=0:
    #     print("Player looses")
    #     return GameState(active_effects, boss_hit, player_hit, player_mana, mana_spent=game_state.mana_spent, spell=None, spellhistory=game_state.spellhistory)

    print(f"- Player has {player_hit} hit points, {player_armor} armor, {player_mana} mana")
    print(f"- Boss has {boss_hit} hit points")
    print(f"Checking active effects : count {len(active_effects)}")
    player_armor = 0
    for eff in active_effects:
        if eff.dmg > 0:
            boss_hit -= eff.dmg
            print(f"{eff.name} deals {eff.dmg} damage; its timer is now {eff.num_turns-1}")
        if eff.heal > 0:
            player_hit += eff.heal
            print(f"{eff.name} heals {eff.heal} health; its timer is now {eff.num_turns-1}")
        if eff.armor> 0:
            player_armor = eff.armor
            print(f"{eff.name} gives {eff.armor} armor; its timer is now {eff.num_turns-1}")
        if eff.mana > 0:
            player_mana += eff.mana
            print(f"{eff.name} gives {eff.mana} mana; its timer is now {eff.num_turns-1}")
    active_effects = [i._replace(num_turns=i.num_turns-1) for i in active_effects]

    active_effects = [i for i in active_effects if i.num_turns > 0]
    if boss_hit <= 0:
        print("Player wins")
        return GameState(active_effects, boss_hit, player_hit, player_mana, mana_spent=game_state.mana_spent, spell=None, spellhistory=game_state.spellhistory)
    if player_armor == 0:
        print(f"- Boss attacks for {BOSS_DAMAGE} hit points")
    else:
        print(f"Boss attacks for {BOSS_DAMAGE} - {player_armor} = {BOSS_DAMAGE - player_armor} damage!")

    player_hit -= (BOSS_DAMAGE - player_armor)
    if player_hit <=0:
        print("Player looses")
        return GameState(active_effects, boss_hit, player_hit, player_mana, mana_spent=game_state.mana_spent, spell=None, spellhistory=game_state.spellhistory)

    return GameState(active_effects, boss_hit, player_hit, player_mana, mana_spent=game_state.mana_spent, spell=None, spellhistory=game_state.spellhistory)




def get_available_spells(gamestate:GameState):
    a = []
    for i in spells:
        if any(x.num_turns > 1 and x.name == i.name for x in gamestate.active_effects):
            pass
        else:
            if gamestate.player_mana >= i.cost:
                a.append(i)
    return a

win = "poison-recharge-shield-poison-magic_missile-magic_missile-magic_missile"
win = "poison-recharge-shield-poison-recharge-shield-poison-magic_missile-magic_missile"
win = "recharge-poison-shield-recharge-poison-shield-magic_missile-poison-magic_missile"
winning = win.split("-")
active_effects, boss_hit, player_hit, player_mana, mana_spent = [], BOSS_HIT, PLAYER_HIT, PLAYER_MANA, 0
starting_state = GameState(active_effects=[], boss_hit=boss_hit, player_hit=player_hit, player_mana=player_mana, mana_spent=0, spell=None, spellhistory="")

gs = starting_state
for w in winning:
    spelli = [i for i in spells if i.name==w]
    av = spelli[0]
    gs = gs._replace(player_mana=gs.player_mana - av.cost,spell=av, mana_spent=av.cost + gs.mana_spent, spellhistory=gs.spellhistory +'-'+av.name)
    gs = play_turn(gs)







min_mana = 9999999
histories = []
winning_history = ""
def solve_game_state(gameState:GameState):
    global min_mana
    global histories
    global winning_history
    if gameState.spell == None:
        available_spells = get_available_spells(gameState)
        for av in available_spells:
            gs = gameState._replace(player_mana=gameState.player_mana - av.cost,spell=av, mana_spent=av.cost + gameState.mana_spent, spellhistory=gameState.spellhistory +'-'+av.name)
            if gs.spellhistory in histories:
                pass
            elif gs.mana_spent > min_mana:
                pass
            else:
                histories.append(gs.spellhistory)
                solve_game_state(gs)
    else:
        gameState = play_turn(gameState)
        if gameState.player_hit <= 0:
            pass
        elif gameState.boss_hit <= 0:
            min_mana = min(min_mana, gameState.mana_spent)
            winning_history = gameState.spellhistory
        elif gameState.mana_spent > min_mana:
            pass
        else:
            solve_game_state(gameState)




solve_game_state(starting_state)

print(min_mana)













