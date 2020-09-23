let addCharge = ( bill ) => {
    if ( bill > 0 ) { 
        return bill * 1.07 
    } else { 
        return 0 ;
     }
};

console.log( addCharge( -1000 ) );static