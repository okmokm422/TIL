let team = [ 'A', 'B', 'C', 'D', 'E' ];
for ( let t1 of team ) {
    for (let t2 of team ) {
        if( t1 != t2 ) {
            console.log( t1 + 'vs' + t2 );
        }
    }
}