set title "magnetic field"
set datafile separator ","
set terminal png
set output "img.png"
unset grid
set xrange [0.0:8.0]
set yrange [0.0:2.0]
set ylabel 'y[cm]'
set xlabel 'x[cm]'
set key right top
#set linestyle 1 lc "black"
#set key box linestyle 1 
set size ratio -1
set palette rgb 33,13,10
adj=0.3
plot "a.csv" using 1:2:(($4/sqrt($3*$3+$4*$4))*adj):(($3/sqrt($3*$3+$4*$4))*adj):(sqrt($3*$3+$4*$4)) with vectors lc palette title "vector[mT]" 
set out
