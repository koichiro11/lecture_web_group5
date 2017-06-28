<div>
    <h3>Create Thread</h3>
    <?= $this->Form->create() ?>
    <fieldset>
    <?php
        echo $this->Form->input('name');
    ?>
    </fieldset>
    <?= $this->Form->button('Create') ?>
    <?= $this->Form->end() ?>
</div>