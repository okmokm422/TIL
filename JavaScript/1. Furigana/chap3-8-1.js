// 総当たり戦の表
let team = [ 'A', 'B', 'C', 'd', 'E' ];

for ( let t1 of team ) {
    for ( let t2 of team ) {
        console.log( t1 + 'vs' + t2 );
    }
}