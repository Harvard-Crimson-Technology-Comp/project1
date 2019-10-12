/** @jsx jsx */
import { jsx } from '@emotion/core';
import { MinimalBase } from '../Base';
import { BuyForm } from '../components/BuyForm';
import { Loading } from '../components/Loading';

export function Buy() {
  const contents = (
    <div>
      <h1>Buy</h1>
      <hr></hr>
      <BuyForm></BuyForm>
      <hr></hr>
    </div>
  );

  return <MinimalBase>{contents}</MinimalBase>
}