import pygame

import gamestate
import graphics
import event
import collisions
import config

was_closed = False
while not was_closed:
    game = gamestate.GameState()
    button_pressed = graphics.draw_main_menu(game)

    if button_pressed == config.play_game_button:
        game.start_pool()
        events = event.events()
        while not (event["closed"] or game.is_game_over or events ["quit_to_main_menu"]):
            events = event.events()
            collisions.resolve_all_collisions(game.balls,game.holes,game.table_sides)
            game.redraw_all()

            if game.all_moving():
                game.check_pool_rules()
                game.cue.make_visible(game.current_player)
                while not(
                        (events["closed"] or events["quit_to_main_meni"]) or game.is_game_over) and game.all_not_moving():
                        game.redraw_all()
                        events = event.events()
                        if game.cue.is_clicked(events):
                            game.cue.cue_is_active(game,events)
                        elif game.can_move_white_ball and game.white_ball.is_clicked(events):
                            game.white_ball.is_active(game,game.is_behind_line_breaak())

        was_closed = events["closed"]

    if button_pressed == config.exit_button:
        was_closed = True
pygame.quit()
