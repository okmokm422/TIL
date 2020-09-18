for ( let rec of data ) {
    let bill = rec['bill'];
    if( rec['crg'] ) {
        bill = addCharge( bill );
    }
    createMail( rec['name'], bill );
}