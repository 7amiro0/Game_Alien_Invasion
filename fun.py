import sys
from time import sleep
import pygame
from bullet import Bullet
from al import Alien
from star import Star


def get_number_rows(ai_set, ship_height, alien_height):
    availabale_space_y = ai_set.he - 2 * alien_height - ship_height
    number_rows = int(availabale_space_y / (1.5 * alien_height))
    return number_rows


def get_number_aliens_x(ai_set, alien_width):
    available_space_y = ai_set.he
    number_aliens_x = int(available_space_y / alien_width) + 1
    return number_aliens_x


def create_alien(ai_set, screen, aliens, alien_number, row_number):
    alien = Alien(ai_set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * 80 * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + 2 * alien.rect.height * row_number) - 80
    aliens.add(alien)


def create_fleet(ai_set, screen, ship, aliens):
    alien = Alien(ai_set, screen)
    number_alien_x = get_number_aliens_x(ai_set, alien.rect.width)
    number_rows = get_number_rows(ai_set, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_set, screen, aliens, alien_number, row_number)


def fire_bullet_player(ai_set, screen, ship, bullets_player):
    if len(bullets_player) <= 3:
        new_bullet = Bullet(ai_set, screen, ship)
        bullets_player.add(new_bullet)


def fire_bullet_helper(ai_set, screen, helper, bullets_helper):
    if len(bullets_helper) < 1:
        new_bullet = Bullet(ai_set, screen, helper)
        bullets_helper.add(new_bullet)


def check_kd(event, ship, bullets, ai_set, screen, stats, sb, button, aliens, helper):
    if event.key == pygame.K_BACKSPACE:
        with open("score.txt", "w") as f:
            last = f
            last.write(str(stats.high_score))
        sys.exit()
    elif event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_j:
        fire_bullet_player(ai_set, screen, ship, bullets)
        fire_bullet_player(ai_set, screen, ship, bullets)
    elif event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_p:
        check_play_button(ai_set, screen, stats, sb, button, ship, aliens, bullets, helper)


def check_ku(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False


def check_play_button(ai_set, screen, stats, sb, button, ship, aliens, bullets, helper):
    if not stats.game_active:
        ai_set.initialize_dinamic_setting()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_lvl()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_set, screen, ship, aliens)
        ship.center_ship()
        helper.center()


def check_event(ship, ai_set, screen, bullets, stats, button, aliens, sb, helper):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kd(event, ship, bullets, ai_set, screen, stats, sb, button, aliens, helper)
        elif event.type == pygame.KEYUP:
            check_ku(event, ship)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_bullets(aliens, bullets_player, screen, ship, ai_set, stats, sb, bullets_helper):
    bullets_player.update()
    for bullet in bullets_player.copy():
        if bullet.rect.bottom <= 0:
            bullets_player.remove(bullet)
    bullets_helper.update()
    for bullet in bullets_helper.copy():
        if bullet.rect.bottom <= 0:
            bullets_helper.remove(bullet)
    collisions_player = pygame.sprite.groupcollide(bullets_player, aliens, True, True)
    collisions_helper = pygame.sprite.groupcollide(bullets_helper, aliens, True, True)
    if collisions_player:
        for aliens in collisions_player.values():
            stats.score += ai_set.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)
    if collisions_helper:
        for aliens in collisions_helper.values():
            stats.score += ai_set.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets_player.empty()
        ai_set.increase_speed()
        stats.level += 1
        sb.prep_lvl()
        create_fleet(ai_set, screen, ship, aliens)


def check_fleet_edges(ai_set, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_set, aliens)
            break


def change_fleet_direction(ai_set,  aliens):
    for alien in aliens.sprites():
        alien.rect.y += 10
    ai_set.fleet_direction *= -1


def check_aliens_bottom(ai_set, stats, screen, ship, aliens, bullets, sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_set, stats, screen, ship, aliens, bullets, sb)
            break


def ship_hit(ai_set, stats, screen, ship, aliens, bullets, sb):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_set, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_set, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_set, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_set, stats, screen, ship, aliens, bullets, sb)
    check_aliens_bottom(ai_set, stats, screen, ship, aliens, bullets, sb)


def create_stars(ai_set, screen, stars):
    for x in range(10):
        star = Star(ai_set, screen)
        stars.add(star)


def update_screen(ai_set, screen, stats, sb, ship, aliens, bullets_player, stars, play_button, helper, bullets_helper):
    screen.fill(ai_set.bgc)
    stars.draw(screen)
    for bullet in bullets_player.sprites():
        bullet.draw_bullet()
    for bullet in bullets_helper.sprites():
        bullet.draw_bullet()
    helper.blit()
    ship.blite()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.time.Clock().tick(1000)
    pygame.display.flip()
