/** @jsx jsx */
import { jsx } from '@emotion/core';
import { MinimalBase } from '../Base';
import { ListForm } from '../components/ListForm';

const imageStyle = {
  borderRadius: "12px"
};

export function List() {
    let contents = (
      <div>
        <h1>List</h1>
        <hr></hr>
        <ListForm></ListForm>
      </div>
    );

  return <MinimalBase>{contents}</MinimalBase>
}