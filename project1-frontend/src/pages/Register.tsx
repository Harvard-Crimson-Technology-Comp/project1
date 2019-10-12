/** @jsx jsx */
import { jsx } from '@emotion/core';
import { MinimalBase } from '../Base';
import { RegisterForm } from '../components/RegisterForm';

export function Register() {
  let contents = (
      <div>
        <h1>Register</h1>
        <hr></hr>
        <RegisterForm></RegisterForm>
        <hr></hr>
      </div>
    );

  return <MinimalBase>{contents}</MinimalBase>
}