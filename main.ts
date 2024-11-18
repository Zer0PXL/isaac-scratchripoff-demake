namespace SpriteKind {
    export const BG = SpriteKind.create()
}
tiles.setCurrentTilemap(tilemap`levelBase`)
let timmy = sprites.create(assets.image`timmy`, SpriteKind.Player)
game.onUpdate(function () {
    controller.moveSprite(timmy)
})
