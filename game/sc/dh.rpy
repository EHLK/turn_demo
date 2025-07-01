
transform bar_shake:
    #matrixtransform RotateMatrix(0,180,0)
    linear 0.05 offset(-2,2)
    linear 0.05 offset(+4,1)
    linear 0.05 offset(-4,-1)
    linear 0.05 offset(+2,2)
    linear 0.05 offset(-1,0)
    linear 0.05 offset(0,0)
init python:
    import pygame
    def draw_line(name, start=(0, 0), end=(100, 100), color="#ff0000", thickness=2):
        # 创建一个新的透明图像
        width = max(start[0], end[0]) - min(start[0], end[0]) + thickness * 2
        height = max(start[1], end[1]) - min(start[1], end[1]) + thickness * 2
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 0))  # 完全透明

        # 转换相对坐标
        rel_start = (start[0] - min(start[0], end[0]) + thickness, start[1] - min(start[1], end[1]) + thickness)
        rel_end = (end[0] - min(start[0], end[0]) + thickness, end[1] - min(start[1], end[1]) + thickness)

        pygame.draw.line(surface, renpy.color(color), rel_start, rel_end, thickness)

        # 将图像注册为 Ren'Py 图像
        renpy.image(name, renpy.DisplayableImageSurface(surface, False))