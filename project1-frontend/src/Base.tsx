/** @jsx jsx */
import React from 'react';
import { jsx, css } from '@emotion/core';
import { Helmet } from 'react-helmet';
import { Link } from 'react-router-dom';

type BaseProps = {
  title?: string;
  children: any;
};

const childContainerStyle = css`
  display: flex;
  justify-content: center;
  margin: 0 auto;
`;

const navFooterStyle = css`
  display: flex;
  justify-content: center;

  ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
  
  li {
    float: left;
  }
  
  li a {
    display: block;
    text-align: center;
    padding: 16px;
    text-decoration: none;
  }
`;

// Most pages should use this minimal base
export function MinimalBase(props: BaseProps) {
  return (
    <React.Fragment>
      <Helmet>
        <title>{"Hello, stocks!"}</title>
      </Helmet>
      <div css={childContainerStyle}>{props.children}</div>
      <div css={navFooterStyle}>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/register">Register</Link></li>
          <li><Link to="/buy">Buy</Link></li>
          <li><Link to="/sell">Sell</Link></li>
          <li><Link to="/list">List</Link></li>
        </ul>
      </div>
    </React.Fragment>
  );
}