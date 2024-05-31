; set soft dips as saved
lea     0xd07320,a0
add.w   0x10fd68,a0
st.b    (a0)
; save soft dips
clr.l   d0
move.w  0x10fd68,d0
lsl.w   #4,d0
lea     0xd07420,a1
add.w   d0,a1
lea     0x108120,a0
move.l  (a0)+,(a1)+
move.l  (a0)+,(a1)+
move.l  (a0)+,(a1)+
move.l  (a0)+,(a1)+
rts