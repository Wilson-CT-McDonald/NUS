import React, { useState } from 'react';
import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';

function BootModal(props) {
  const [modal, setModal] = useState(false);

  const toggle = () => setModal(!modal);

  return (
    <div>
      <Button color={props.color1} onClick={toggle}>
        {props.name1}
      </Button>
      <Modal isOpen={modal} toggle={toggle} {...props}>
        <ModalHeader toggle={toggle}>Modal title</ModalHeader>
        <ModalBody>
          {props.mbody}
        </ModalBody>
        <ModalFooter>
          <Button color={props.color2} onClick={toggle}>
            {props.name2}
          </Button>{' '}
          <Button color={props.color3} onClick={toggle}>
            {props.name3}
          </Button>
        </ModalFooter>
      </Modal>
    </div>
  );
}

export default BootModal;