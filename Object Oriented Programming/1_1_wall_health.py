def destroy_walls(wall_health):
    health = []
    for wall in wall_health:
        if wall > 0:
            health.append(wall)
    return health
