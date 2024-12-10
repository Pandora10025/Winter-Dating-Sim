# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


transform frost_particles(delay):

    zoom 2.0 alpha 0.0 yoffset 0 xoffset 0 rotate 0

    pause delay

    parallel:
        linear 2.0 alpha 0.5
        linear 2.0 alpha 0.0

    parallel:
        easein 4.0 xoffset -150

    parallel:
        choice:
            easein 4.0 yoffset 10
        choice:
            easein 4.0 yoffset 0
        choice:
            easein 4.0 yoffset -10

    parallel:
        choice:
            easein 4.0 rotate 5
        choice:
            easein 4.0 rotate 0
        choice:
            easein 4.0 rotate -5


image frost_particles = Composite(
    (200,200),
    (0,0), At("frost_breath/p2.png", frost_particles(0.0)),
    (0,0), At("frost_breath/p3.png", frost_particles(0.1)),
    (0,0), At("frost_breath/p4.png", frost_particles(0.2)),
    (0,0), At("frost_breath/p1.png", frost_particles(0.3)),
    (0,0), At("frost_breath/p5.png", frost_particles(0.4)))


image frost_breath:
    "frost_particles"
    choice:
        pause 6.0
    choice:
        pause 7.0
    choice:
        pause 8.0
    repeat
