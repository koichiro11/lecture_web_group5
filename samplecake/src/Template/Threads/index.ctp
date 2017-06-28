<div>
	<h3>Threads List</h3>
	<?php foreach ($threads as $thread): ?>
	<tr>
		<td><?=  h($thread->id) ?></td>
		<td><?= h($thread->name) ?></td>
	</tr>
	<?php endforeach; ?>

	</form>
</div>