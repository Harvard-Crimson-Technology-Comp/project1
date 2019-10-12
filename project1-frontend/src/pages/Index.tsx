/** @jsx jsx */
import { jsx } from '@emotion/core';
import { MinimalBase } from '../Base';
import { gql } from 'apollo-boost';
import { useQuery } from '@apollo/react-hooks';
import { Loading } from '../components/Loading';
import { objectTypeSpreadProperty } from '@babel/types';

const imageStyle = {
  borderRadius: "12px"
};

const STATS_QUERY = gql`
  query {
    users {
      id
      username
    }
    stocks {
      symbol
      quantity
    }
    portfolios {
      cash
    }
  }
`;

export function Index() {
  let contents;

  const { loading, error, data } = useQuery(STATS_QUERY);

  if (loading) {
    contents = <Loading></Loading>;
  }
  else if (error) {
    contents = <p>{error}</p>;
  } else {
    let total_cash = data.portfolios.reduce((sum: number, x: any) => sum + parseFloat(x.cash), 0.0);

    let num_users: number = data.users.length;
    let usernames: any = data.users.map((user: any) => <li>{user.username}</li>);

    let stocks: any = {};

    data.stocks.forEach((stock: any) => {
      if (stocks.hasOwnProperty(stock.symbol)) {
        stocks[stock.symbol] += stock.quantity;
      } else {
        stocks[stock.symbol] = stock.quantity;
      }
    });

    let stocks_html = Object.keys(stocks).map((symbol: string) => <li>{symbol} - {stocks[symbol]}</li>);

    contents = (
      <div>
        <hr></hr>
        <h1>Hello! Welcome to our Stocks App!</h1>
        <hr></hr>
        <p>We've set up some basic skeleton code to get you going!</p>
        <p>Feel free to look around and get acquainted with the flow of things.</p>
        <p>In particular, look at the following:</p>
        <ul>
          <li><i>routes.tsx</i> - tells React what to do with different requests</li>
          <li><i>App.js</i> - the main React App - sets up a lot of the stuff we need, like the Router and Apollo</li>
          <li><i>Base.tsx</i> - the base template for each page, sets up our style and layout</li>
          <li><i>pages/Index.tsx</i> - this page</li>
        </ul>
        <img style={imageStyle} src="https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftr1.cbsistatic.com%2Fhub%2Fi%2F2017%2F07%2F06%2F86b50b09-d769-4e1f-9e57-822da0b86d44%2Fd2d5ab16c8e198e1bfeb79adbd48e25b%2Fapplememes-stock.jpg&f=1&nofb=1"/>
        <hr></hr>
        <p>This page should be informational.</p>
        <p>You can also display stats or things here if you want.</p>
        <hr></hr>
        <p>Total Cash: ${total_cash.toFixed(2)}</p>
        <p>Cash/Users: ${(total_cash / num_users).toFixed(2)}</p>
        <p>Number of Users: {num_users}</p>
        <p>Usernames:</p>
        <ol>
          {usernames}
        </ol>
        <p>Stocks:</p>
        <ul>
          {stocks_html}
        </ul>
      </div>
    );
  }

  return <MinimalBase>{contents}</MinimalBase>
}