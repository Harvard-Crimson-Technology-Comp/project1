/** @jsx jsx */
import { jsx } from '@emotion/core';
import { gql } from 'apollo-boost';
import { useQuery } from '@apollo/react-hooks';
import React from 'react';
import fetch from 'node-fetch';

type FormProps = {};

type FormState = {
    api_token: string,
    result: any
};

const resultStyle = {
    "word-break": "break-all",
    "padding": "20px"
};

function encodedParams(state: any) {
    let s = Object.keys(state).map((k) => 
        encodeURIComponent(k) + '=' + encodeURIComponent(state[k])
    ).join('&');

    return s;
}

export class ListForm extends React.Component<FormProps, FormState> {
    constructor(props: any) {
        super(props);
        this.state = {
            api_token: '',
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
        fetch('http://127.0.0.1:8000/api/list?' + encodedParams(this.state))
        .then(function (result: any) { return result.json(); })
        .then((result: any) => 
            this.setState({
                "result": result
            }));

        event.preventDefault();
    }

    render() {
        let children;

        if (this.state.result) {
            if (this.state.result.hasOwnProperty("error")) {
                children = <p>Error: {this.state.result.error}</p>;
            } else {
                children = this.state.result.stocks.map((stock: any) => 
                    <p>Symbol: {stock.symbol}, Quantity: {stock.quantity}, Price: ${stock.price}</p>
                );

                children.push(<p>Total Value: ${this.state.result.total_value}</p>);
            }
        }

        return (
            <>
                <div style={resultStyle}>
                    {children}
                </div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        API Key:
                        <input type="text" name="api_token" value={this.state.api_token} onChange={this.handleChange} />
                    </label>
                    <br />
                    <input type="submit" value="submit"/>
                </form>
            </>
        );
    }
}
