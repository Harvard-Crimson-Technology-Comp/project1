import React from 'react';
import { Index } from './pages/Index';
import { Register } from './pages/Register';
import { List } from './pages/List';
import { Sell } from './pages/Sell';
import { Buy } from './pages/Buy';

// a helper function which makes writing routes more convenient
function route(
  name: string,
  path: string,
  component: React.ComponentType<any>,
  exact = true
) {
  return { name, path, component, exact };
}

// a list of all the url patterns that we will support
export const routes = [
  route('index', '/', Index),
  route('register', '/register', Register),
  route('list', '/list', List),
  route('sell', '/sell', Sell),
  route('buy', '/buy', Buy)
];