import {useState, useEffect} from 'react';

const CharacterCounter = () => {
    const [text, setText] = useState('');
    const [error, setErrror] = useState('');

    useEffect(() => {
        if (text.length>5) {
            setErrror("Text is greater than 5 characters!");
        }
    }, [text]);


    return (
        <>
            <h1>Hola </h1>
            <input type="text" value={text} onChange={(e)=>setText(e.target.value)} />
            Here is your text: {text}
            {error && <div style={{backgroundColor:'red'}}>{error}</div>}
        </>
    )

}

export default CharacterCounter;