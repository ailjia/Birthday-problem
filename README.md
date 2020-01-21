# Birthday-problem

Birthday problem is well-known problem in probability theory. The objective is to find the probability that some people in a room will have the same birthday. 

The problem is only solvable by a simplified assumption: that each day is equally likely for a birthday. For this reason, 29 Feb is excluded and there are 365 possible birthdays in a year.

The mathematical definition of the problem is as follows:
Find the probability P(A) that at least two people in the room have the same birthday. It is easier to calculate the probability that none of the people in the room have the same birthday, which is represented by P(A′) = 1 - P(A).

Now given the number of people n, we can use p(n) to denote the probability of at least two out of the n people having the same birthday. Similarly, it is easier to first calculate the probability p(n) that all n birthdays are different. 
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="60.813ex" height="22.176ex" style="vertical-align: -10.505ex;" viewBox="0 -5025.1 26183.5 9547.9" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" aria-labelledby="MathJax-SVG-1-Title">
<title id="MathJax-SVG-1-Title">{\displaystyle {\begin{aligned}{\bar {p}}(n)&amp;=1\times \left(1-{\frac {1}{365}}\right)\times \left(1-{\frac {2}{365}}\right)\times \cdots \times \left(1-{\frac {n-1}{365}}\right)\\[6pt]&amp;={\frac {365\times 364\times \cdots \times (365-n+1)}{365^{n}}}\\[6pt]&amp;={\frac {365!}{365^{n}(365-n)!}}={\frac {n!\cdot {\binom {365}{n}}}{365^{n}}}={\frac {_{365}P_{n}}{365^{n}}}\end{aligned}}}</title>
<defs aria-hidden="true">
<path stroke-width="1" id="E1-MJMATHI-70" d="M23 287Q24 290 25 295T30 317T40 348T55 381T75 411T101 433T134 442Q209 442 230 378L240 387Q302 442 358 442Q423 442 460 395T497 281Q497 173 421 82T249 -10Q227 -10 210 -4Q199 1 187 11T168 28L161 36Q160 35 139 -51T118 -138Q118 -144 126 -145T163 -148H188Q194 -155 194 -157T191 -175Q188 -187 185 -190T172 -194Q170 -194 161 -194T127 -193T65 -192Q-5 -192 -24 -194H-32Q-39 -187 -39 -183Q-37 -156 -26 -148H-6Q28 -147 33 -136Q36 -130 94 103T155 350Q156 355 156 364Q156 405 131 405Q109 405 94 377T71 316T59 280Q57 278 43 278H29Q23 284 23 287ZM178 102Q200 26 252 26Q282 26 310 49T356 107Q374 141 392 215T411 325V331Q411 405 350 405Q339 405 328 402T306 393T286 380T269 365T254 350T243 336T235 326L232 322Q232 321 229 308T218 264T204 212Q178 106 178 102Z"></path>
<path stroke-width="1" id="E1-MJMAIN-AF" d="M69 544V590H430V544H69Z"></path>
<path stroke-width="1" id="E1-MJMAIN-28" d="M94 250Q94 319 104 381T127 488T164 576T202 643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275 667T226 581T184 443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318 -250H315H302L274 -226Q180 -141 137 -14T94 250Z"></path>
<path stroke-width="1" id="E1-MJMATHI-6E" d="M21 287Q22 293 24 303T36 341T56 388T89 425T135 442Q171 442 195 424T225 390T231 369Q231 367 232 367L243 378Q304 442 382 442Q436 442 469 415T503 336T465 179T427 52Q427 26 444 26Q450 26 453 27Q482 32 505 65T540 145Q542 153 560 153Q580 153 580 145Q580 144 576 130Q568 101 554 73T508 17T439 -10Q392 -10 371 17T350 73Q350 92 386 193T423 345Q423 404 379 404H374Q288 404 229 303L222 291L189 157Q156 26 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 112 180T152 343Q153 348 153 366Q153 405 129 405Q91 405 66 305Q60 285 60 284Q58 278 41 278H27Q21 284 21 287Z"></path>
<path stroke-width="1" id="E1-MJMAIN-29" d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641 251 514T294 250Q294 182 284 119T261 12T224 -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86 -250H74Q66 -250 63 -250T58 -247T55 -238Q56 -237 66 -225Q221 -64 221 250T66 725Q56 737 55 738Q55 746 60 749Z"></path>
<path stroke-width="1" id="E1-MJMAIN-3D" d="M56 347Q56 360 70 367H707Q722 359 722 347Q722 336 708 328L390 327H72Q56 332 56 347ZM56 153Q56 168 72 173H708Q722 163 722 153Q722 140 707 133H70Q56 140 56 153Z"></path>
<path stroke-width="1" id="E1-MJMAIN-31" d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z"></path>
<path stroke-width="1" id="E1-MJMAIN-D7" d="M630 29Q630 9 609 9Q604 9 587 25T493 118L389 222L284 117Q178 13 175 11Q171 9 168 9Q160 9 154 15T147 29Q147 36 161 51T255 146L359 250L255 354Q174 435 161 449T147 471Q147 480 153 485T168 490Q173 490 175 489Q178 487 284 383L389 278L493 382Q570 459 587 475T609 491Q630 491 630 471Q630 464 620 453T522 355L418 250L522 145Q606 61 618 48T630 29Z"></path>
<path stroke-width="1" id="E1-MJMAIN-2212" d="M84 237T84 250T98 270H679Q694 262 694 250T679 230H98Q84 237 84 250Z"></path>
<path stroke-width="1" id="E1-MJMAIN-33" d="M127 463Q100 463 85 480T69 524Q69 579 117 622T233 665Q268 665 277 664Q351 652 390 611T430 522Q430 470 396 421T302 350L299 348Q299 347 308 345T337 336T375 315Q457 262 457 175Q457 96 395 37T238 -22Q158 -22 100 21T42 130Q42 158 60 175T105 193Q133 193 151 175T169 130Q169 119 166 110T159 94T148 82T136 74T126 70T118 67L114 66Q165 21 238 21Q293 21 321 74Q338 107 338 175V195Q338 290 274 322Q259 328 213 329L171 330L168 332Q166 335 166 348Q166 366 174 366Q202 366 232 371Q266 376 294 413T322 525V533Q322 590 287 612Q265 626 240 626Q208 626 181 615T143 592T132 580H135Q138 579 143 578T153 573T165 566T175 555T183 540T186 520Q186 498 172 481T127 463Z"></path>
<path stroke-width="1" id="E1-MJMAIN-36" d="M42 313Q42 476 123 571T303 666Q372 666 402 630T432 550Q432 525 418 510T379 495Q356 495 341 509T326 548Q326 592 373 601Q351 623 311 626Q240 626 194 566Q147 500 147 364L148 360Q153 366 156 373Q197 433 263 433H267Q313 433 348 414Q372 400 396 374T435 317Q456 268 456 210V192Q456 169 451 149Q440 90 387 34T253 -22Q225 -22 199 -14T143 16T92 75T56 172T42 313ZM257 397Q227 397 205 380T171 335T154 278T148 216Q148 133 160 97T198 39Q222 21 251 21Q302 21 329 59Q342 77 347 104T352 209Q352 289 347 316T329 361Q302 397 257 397Z"></path>
<path stroke-width="1" id="E1-MJMAIN-35" d="M164 157Q164 133 148 117T109 101H102Q148 22 224 22Q294 22 326 82Q345 115 345 210Q345 313 318 349Q292 382 260 382H254Q176 382 136 314Q132 307 129 306T114 304Q97 304 95 310Q93 314 93 485V614Q93 664 98 664Q100 666 102 666Q103 666 123 658T178 642T253 634Q324 634 389 662Q397 666 402 666Q410 666 410 648V635Q328 538 205 538Q174 538 149 544L139 546V374Q158 388 169 396T205 412T256 420Q337 420 393 355T449 201Q449 109 385 44T229 -22Q148 -22 99 32T50 154Q50 178 61 192T84 210T107 214Q132 214 148 197T164 157Z"></path>
<path stroke-width="1" id="E1-MJSZ3-28" d="M701 -940Q701 -943 695 -949H664Q662 -947 636 -922T591 -879T537 -818T475 -737T412 -636T350 -511T295 -362T250 -186T221 17T209 251Q209 962 573 1361Q596 1386 616 1405T649 1437T664 1450H695Q701 1444 701 1441Q701 1436 681 1415T629 1356T557 1261T476 1118T400 927T340 675T308 359Q306 321 306 250Q306 -139 400 -430T690 -924Q701 -936 701 -940Z"></path>
<path stroke-width="1" id="E1-MJSZ3-29" d="M34 1438Q34 1446 37 1448T50 1450H56H71Q73 1448 99 1423T144 1380T198 1319T260 1238T323 1137T385 1013T440 864T485 688T514 485T526 251Q526 134 519 53Q472 -519 162 -860Q139 -885 119 -904T86 -936T71 -949H56Q43 -949 39 -947T34 -937Q88 -883 140 -813Q428 -430 428 251Q428 453 402 628T338 922T245 1146T145 1309T46 1425Q44 1427 42 1429T39 1433T36 1436L34 1438Z"></path>
<path stroke-width="1" id="E1-MJMAIN-32" d="M109 429Q82 429 66 447T50 491Q50 562 103 614T235 666Q326 666 387 610T449 465Q449 422 429 383T381 315T301 241Q265 210 201 149L142 93L218 92Q375 92 385 97Q392 99 409 186V189H449V186Q448 183 436 95T421 3V0H50V19V31Q50 38 56 46T86 81Q115 113 136 137Q145 147 170 174T204 211T233 244T261 278T284 308T305 340T320 369T333 401T340 431T343 464Q343 527 309 573T212 619Q179 619 154 602T119 569T109 550Q109 549 114 549Q132 549 151 535T170 489Q170 464 154 447T109 429Z"></path>
<path stroke-width="1" id="E1-MJMAIN-22EF" d="M78 250Q78 274 95 292T138 310Q162 310 180 294T199 251Q199 226 182 208T139 190T96 207T78 250ZM525 250Q525 274 542 292T585 310Q609 310 627 294T646 251Q646 226 629 208T586 190T543 207T525 250ZM972 250Q972 274 989 292T1032 310Q1056 310 1074 294T1093 251Q1093 226 1076 208T1033 190T990 207T972 250Z"></path>
<path stroke-width="1" id="E1-MJMAIN-34" d="M462 0Q444 3 333 3Q217 3 199 0H190V46H221Q241 46 248 46T265 48T279 53T286 61Q287 63 287 115V165H28V211L179 442Q332 674 334 675Q336 677 355 677H373L379 671V211H471V165H379V114Q379 73 379 66T385 54Q393 47 442 46H471V0H462ZM293 211V545L74 212L183 211H293Z"></path>
<path stroke-width="1" id="E1-MJMAIN-2B" d="M56 237T56 250T70 270H369V420L370 570Q380 583 389 583Q402 583 409 568V270H707Q722 262 722 250T707 230H409V-68Q401 -82 391 -82H389H387Q375 -82 369 -68V230H70Q56 237 56 250Z"></path>
<path stroke-width="1" id="E1-MJMAIN-21" d="M78 661Q78 682 96 699T138 716T180 700T199 661Q199 654 179 432T158 206Q156 198 139 198Q121 198 119 206Q118 209 98 431T78 661ZM79 61Q79 89 97 105T141 121Q164 119 181 104T198 61Q198 31 181 16T139 1Q114 1 97 16T79 61Z"></path>
<path stroke-width="1" id="E1-MJMAIN-22C5" d="M78 250Q78 274 95 292T138 310Q162 310 180 294T199 251Q199 226 182 208T139 190T96 207T78 250Z"></path>
<path stroke-width="1" id="E1-MJSZ1-28" d="M152 251Q152 646 388 850H416Q422 844 422 841Q422 837 403 816T357 753T302 649T255 482T236 250Q236 124 255 19T301 -147T356 -251T403 -315T422 -340Q422 -343 416 -349H388Q359 -325 332 -296T271 -213T212 -97T170 56T152 251Z"></path>
<path stroke-width="1" id="E1-MJSZ1-29" d="M305 251Q305 -145 69 -349H56Q43 -349 39 -347T35 -338Q37 -333 60 -307T108 -239T160 -136T204 27T221 250T204 473T160 636T108 740T60 807T35 839Q35 850 50 850H56H69Q197 743 256 566Q305 425 305 251Z"></path>
<path stroke-width="1" id="E1-MJMATHI-50" d="M287 628Q287 635 230 637Q206 637 199 638T192 648Q192 649 194 659Q200 679 203 681T397 683Q587 682 600 680Q664 669 707 631T751 530Q751 453 685 389Q616 321 507 303Q500 302 402 301H307L277 182Q247 66 247 59Q247 55 248 54T255 50T272 48T305 46H336Q342 37 342 35Q342 19 335 5Q330 0 319 0Q316 0 282 1T182 2Q120 2 87 2T51 1Q33 1 33 11Q33 13 36 25Q40 41 44 43T67 46Q94 46 127 49Q141 52 146 61Q149 65 218 339T287 628ZM645 554Q645 567 643 575T634 597T609 619T560 635Q553 636 480 637Q463 637 445 637T416 636T404 636Q391 635 386 627Q384 621 367 550T332 412T314 344Q314 342 395 342H407H430Q542 342 590 392Q617 419 631 471T645 554Z"></path>
</defs>
<g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)" aria-hidden="true">
<g transform="translate(167,0)">
<g transform="translate(-11,0)">
<g transform="translate(0,3440)">
 <use xlink:href="#E1-MJMATHI-70" x="0" y="0"></use>
 <use xlink:href="#E1-MJMAIN-AF" x="84" y="8"></use>
 <use xlink:href="#E1-MJMAIN-28" x="585" y="0"></use>
 <use xlink:href="#E1-MJMATHI-6E" x="974" y="0"></use>
 <use xlink:href="#E1-MJMAIN-29" x="1575" y="0"></use>
</g>
</g>
<g transform="translate(1954,0)">
<g transform="translate(0,3440)">
 <use xlink:href="#E1-MJMAIN-3D" x="277" y="0"></use>
 <use xlink:href="#E1-MJMAIN-31" x="1334" y="0"></use>
 <use xlink:href="#E1-MJMAIN-D7" x="2056" y="0"></use>
<g transform="translate(3057,0)">
 <use xlink:href="#E1-MJSZ3-28"></use>
<g transform="translate(736,0)">
 <use xlink:href="#E1-MJMAIN-31" x="0" y="0"></use>
 <use xlink:href="#E1-MJMAIN-2212" x="722" y="0"></use>
<g transform="translate(1723,0)">
<g transform="translate(120,0)">
<rect stroke="none" width="1621" height="60" x="0" y="220"></rect>
 <use xlink:href="#E1-MJMAIN-31" x="560" y="676"></use>
<g transform="translate(60,-687)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
</g>
</g>
</g>
</g>
 <use xlink:href="#E1-MJSZ3-29" x="4321" y="-1"></use>
</g>
 <use xlink:href="#E1-MJMAIN-D7" x="8337" y="0"></use>
<g transform="translate(9338,0)">
 <use xlink:href="#E1-MJSZ3-28"></use>
<g transform="translate(736,0)">
 <use xlink:href="#E1-MJMAIN-31" x="0" y="0"></use>
 <use xlink:href="#E1-MJMAIN-2212" x="722" y="0"></use>
<g transform="translate(1723,0)">
<g transform="translate(120,0)">
<rect stroke="none" width="1621" height="60" x="0" y="220"></rect>
 <use xlink:href="#E1-MJMAIN-32" x="560" y="676"></use>
<g transform="translate(60,-687)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
</g>
</g>
</g>
</g>
 <use xlink:href="#E1-MJSZ3-29" x="4321" y="-1"></use>
</g>
 <use xlink:href="#E1-MJMAIN-D7" x="14618" y="0"></use>
 <use xlink:href="#E1-MJMAIN-22EF" x="15619" y="0"></use>
 <use xlink:href="#E1-MJMAIN-D7" x="17014" y="0"></use>
<g transform="translate(18014,0)">
 <use xlink:href="#E1-MJSZ3-28"></use>
<g transform="translate(736,0)">
 <use xlink:href="#E1-MJMAIN-31" x="0" y="0"></use>
 <use xlink:href="#E1-MJMAIN-2212" x="722" y="0"></use>
<g transform="translate(1723,0)">
<g transform="translate(120,0)">
<rect stroke="none" width="2443" height="60" x="0" y="220"></rect>
<g transform="translate(60,676)">
 <use xlink:href="#E1-MJMATHI-6E" x="0" y="0"></use>
 <use xlink:href="#E1-MJMAIN-2212" x="822" y="0"></use>
 <use xlink:href="#E1-MJMAIN-31" x="1823" y="0"></use>
</g>
<g transform="translate(471,-687)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
</g>
</g>
</g>
</g>
 <use xlink:href="#E1-MJSZ3-29" x="5143" y="-1"></use>
</g>
</g>
<g transform="translate(0,68)">
 <use xlink:href="#E1-MJMAIN-3D" x="277" y="0"></use>
<g transform="translate(1334,0)">
<g transform="translate(120,0)">
<rect stroke="none" width="13791" height="60" x="0" y="220"></rect>
<g transform="translate(60,770)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
 <use xlink:href="#E1-MJMAIN-D7" x="1723" y="0"></use>
<g transform="translate(2724,0)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-34" x="1001" y="0"></use>
</g>
 <use xlink:href="#E1-MJMAIN-D7" x="4448" y="0"></use>
 <use xlink:href="#E1-MJMAIN-22EF" x="5448" y="0"></use>
 <use xlink:href="#E1-MJMAIN-D7" x="6843" y="0"></use>
 <use xlink:href="#E1-MJMAIN-28" x="7844" y="0"></use>
<g transform="translate(8233,0)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
</g>
 <use xlink:href="#E1-MJMAIN-2212" x="9957" y="0"></use>
 <use xlink:href="#E1-MJMATHI-6E" x="10958" y="0"></use>
 <use xlink:href="#E1-MJMAIN-2B" x="11781" y="0"></use>
 <use xlink:href="#E1-MJMAIN-31" x="12781" y="0"></use>
 <use xlink:href="#E1-MJMAIN-29" x="13282" y="0"></use>
</g>
<g transform="translate(5882,-728)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-6E" x="2123" y="557"></use>
</g>
</g>
</g>
</g>
<g transform="translate(0,-3370)">
 <use xlink:href="#E1-MJMAIN-3D" x="277" y="0"></use>
<g transform="translate(1334,0)">
<g transform="translate(120,0)">
<rect stroke="none" width="6528" height="60" x="0" y="220"></rect>
<g transform="translate(2374,676)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
 <use xlink:href="#E1-MJMAIN-21" x="1501" y="0"></use>
</g>
<g transform="translate(60,-771)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-6E" x="2123" y="557"></use>
 <use xlink:href="#E1-MJMAIN-28" x="2026" y="0"></use>
<g transform="translate(2415,0)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
</g>
 <use xlink:href="#E1-MJMAIN-2212" x="4139" y="0"></use>
 <use xlink:href="#E1-MJMATHI-6E" x="5140" y="0"></use>
 <use xlink:href="#E1-MJMAIN-29" x="5740" y="0"></use>
 <use xlink:href="#E1-MJMAIN-21" x="6130" y="0"></use>
</g>
</g>
</g>
 <use xlink:href="#E1-MJMAIN-3D" x="8380" y="0"></use>
<g transform="translate(9436,0)">
<g transform="translate(120,0)">
<rect stroke="none" width="3700" height="60" x="0" y="220"></rect>
<g transform="translate(60,872)">
 <use xlink:href="#E1-MJMATHI-6E" x="0" y="0"></use>
 <use xlink:href="#E1-MJMAIN-21" x="600" y="0"></use>
 <use xlink:href="#E1-MJMAIN-22C5" x="1101" y="0"></use>
<g transform="translate(1601,0)">
 <use xlink:href="#E1-MJSZ1-28" x="0" y="-1"></use>
<g transform="translate(458,0)">
<g transform="translate(0,443)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-33"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
</g>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-6E" x="450" y="-488"></use>
</g>
 <use xlink:href="#E1-MJSZ1-29" x="1520" y="-1"></use>
</g>
</g>
<g transform="translate(837,-728)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-6E" x="2123" y="557"></use>
</g>
</g>
</g>
 <use xlink:href="#E1-MJMAIN-3D" x="13655" y="0"></use>
<g transform="translate(14711,0)">
<g transform="translate(120,0)">
<rect stroke="none" width="2448" height="60" x="0" y="220"></rect>
<g transform="translate(60,685)">
<g transform="translate(0,-150)">
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-33"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
</g>
<g transform="translate(1161,0)">
 <use xlink:href="#E1-MJMATHI-50" x="0" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-6E" x="908" y="-213"></use>
</g>
</g>
<g transform="translate(211,-728)">
 <use xlink:href="#E1-MJMAIN-33"></use>
 <use xlink:href="#E1-MJMAIN-36" x="500" y="0"></use>
 <use xlink:href="#E1-MJMAIN-35" x="1001" y="0"></use>
 <use transform="scale(0.707)" xlink:href="#E1-MJMATHI-6E" x="2123" y="557"></use>
</g>
</g>
</g>
</g>
</g>
</g>
</g>
</svg>
The codes provided are to calculate the probability of the birthday problem, given the number of people in the room. 
