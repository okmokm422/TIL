let moji = prompt( '年齢は？' );
if ( ! isNaN( moji ) ){
    let age = parseInt( moji );
    if( age < 20 ) {
        console.log( '未成年' );
    }
}