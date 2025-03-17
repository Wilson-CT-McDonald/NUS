import React from 'react';
import { Button } from 'reactstrap';

export function BootButton(props) {
    return <Button color={props.color}>{props.name}</Button>;
}

export function WelcomeMessage({name}) {
    return (
        <div> 
            <h1>Welcome, {name}!</h1>
        </div>
    )
}