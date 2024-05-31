; check if saved
clr.l   d0
move.w  0x10fd68,d0
lea     0xd07320,a1
add.w   d0,a1
lsl.w   #4,d0
lea     0xd07420,a0
add.w   d0,a0
tst.b   (a1)
bne     copy
; load from cartridge
jsr     0xc04418        ; switch to new game
jsr     0xc11612        ; load default soft dips from cartridge
lea     0x10fd84,a0
copy:
; copy to expected location
lea     0x108120,a1
move.l  (a0)+,(a1)+
move.l  (a0)+,(a1)+
move.l  (a0)+,(a1)+
move.l  (a0)+,(a1)+
rts