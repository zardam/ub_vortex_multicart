;move.w    0x10fd68,d0
;addq.w    #1,d0

check_overflow:
cmp.w     #0x9e,d0
blt.b     evict
subi.w    #0x9e,d0

evict:
cmp.w     #154,d0   ; XEVIOUS (stuck on splash screen)
beq       next
cmp.w     #126,d0   ; THE EYE OF TYPHOON (crash)
beq       next

bra       exit
next:
addq.w    #1,d0
bra       check_overflow

exit:
jmp      0xc0a5ce