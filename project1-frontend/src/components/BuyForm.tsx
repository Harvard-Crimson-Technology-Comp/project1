/** @jsx jsx */
import { jsx } from '@emotion/core';
import React from 'react';
import fetch from 'node-fetch';

type FormProps = {};

type FormState = {
    api_token: string,
    symbol: string,
    quantity: string,
    result: any
};

const resultStyle = {
    "word-break": "break-all",
    "padding": "20px"
};

export class BuyForm extends React.Component<FormProps, FormState> {
    constructor(props: any) {
        super(props);
        this.state = {
            api_token: '',
            symbol: '',
            quantity: '',
            result: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event: any) {
        const target: any = event.target;
        const name: FormState = target.name;
        const value: FormState = target.value;

        this.setState({
            // @ts-ignore
            [name]: value
        });
    }

    handleSubmit(event: any) {
        let formData = new FormData();
        for (var key in this.state) {
            // @ts-ignore
            formData.append(key, this.state[key]);
        }

        // @ts-ignore
        fetch('http://127.0.0.1:8000/api/buy', {
            method: 'POST',
            body: formData
        })
        .then(function (result: any) { return result.json(); })
        .then((result: any) => 
            this.setState({
                "result": JSON.stringify(result),
                "symbol": '',
                "quantity": ''
            }));

        event.preventDefault();
    }

    render() {
        return (
            <>
                <div style={resultStyle}>
                    <p>{this.state.result}</p>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        API Key:
                        <input type="text" name="api_token" value={this.state.api_token} onChange={this.handleChange} />
                    </label>
                    <br />
                    <label>
                        Symbol: 
                        <input type="text" name="symbol" value={this.state.symbol} onChange={this.handleChange} />
                    </label>
                    <br/>
                    <label>
                        Quantity 
                        <input type="number" name="quantity" value={this.state.quantity} onChange={this.handleChange} />
                    </label>
                    <br/>
                    <input type="submit" value="submit"/>
                </form>
            </>
        );
    }
}
