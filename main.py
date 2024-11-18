mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . f f f f . . . . . . 
            . . . . f f f d d f f . . . . . 
            . . . f f d d d d d f f . . . . 
            . . . f d f d d d f d f . . . . 
            . . . f d 9 d d d 9 d f . . . . 
            . . . f 9 d d d d d 9 f . . . . 
            . . . f 9 d f f f d 9 f . . . . 
            . . . . f f d d d f f f . . . . 
            . . . . . f f f f f . . . . . . 
            . . . . . . f d f . . . . . . . 
            . . . . . f f d f f . . . . . . 
            . . . . f . f d f . f . . . . . 
            . . . . . . f d f . . . . . . . 
            . . . . . . f f f . . . . . . . 
            . . . . . f . . . f . . . . . .
    """),
    SpriteKind.player)

def on_on_update():
    controller.move_sprite(mySprite)
game.on_update(on_on_update)
