let moji = prompt( '年齢は？' );
if( ! isNaN( moji ) ) {
    let age  = parseInt( moji );
    if( age < 20 ) {
        console.log( '未成年' );
    } else if( age < 65 ) {
        console.log( '成人' );
    } else {
        console.log( '高齢者' )
    }
}