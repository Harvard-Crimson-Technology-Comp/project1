/** @jsx jsx */
import { jsx } from '@emotion/core';
import { MinimalBase } from '../Base';
import { SellForm } from '../components/SellForm';

export function Sell() {
  const contents = (
    <div>
      <h1>Sell</h1>
      <hr></hr>
      <SellForm></SellForm>
      <hr></hr>
    </div>
  );

  return <MinimalBase>{contents}</MinimalBase>
}