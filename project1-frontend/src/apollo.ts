import {
    IntrospectionFragmentMatcher,
    InMemoryCache,
  } from 'apollo-cache-inmemory';
  import ApolloClient from 'apollo-boost';
  import introspectionQueryResultData from './fragmentTypes.json';
  
  const fragmentMatcher = new IntrospectionFragmentMatcher({
    introspectionQueryResultData,
  });
  
  function createCache() {
    return new InMemoryCache({ fragmentMatcher });
  }
  
  function createClientHelper(cache: InMemoryCache) {
    return new ApolloClient({
      cache,
      uri: 'http://127.0.0.1:8000/graphql',
    });
  }
  
  export function createClient() {
    return createClientHelper(createCache());
  }