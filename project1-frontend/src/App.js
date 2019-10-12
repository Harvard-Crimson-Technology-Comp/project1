/** @jsx jsx */
import { ApolloProvider } from '@apollo/react-hooks';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { createClient } from './apollo';
import { routes } from './routes';
import { jsx } from '@emotion/core';

const client = createClient();

function App() {
  return (
    <ApolloProvider client={client}>
      <BrowserRouter>
        {<Switch>
          {routes.map(route => (
            <Route {...route} key={route.path} />
          ))}
        </Switch>}
      </BrowserRouter>
    </ApolloProvider>
  );
}

export default App;