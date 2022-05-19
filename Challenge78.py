def kill_monsters(health, monsters, damage):
    hits = (monsters-1)//3
    d = damage * hits
    if health - d <= 0: return 'hero died'
    return f"hits: {hits}, damage: {d}, health: {health - d}"


print(kill_monsters(50, 7, 10))