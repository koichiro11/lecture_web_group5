<?php
namespace App\Controller;
 
use App\Controller\AppController;
 
class SampleController extends AppController
{
	public function index()
	{
		$str = $this->request->data('text1');
		$msg = 'typed: ' . $str;
		if ($str == null) 
			{ $msg = "please type..."; }
		$this->set('message', $msg);
		$this->set('threads', $this->Threads->find('all'));
	}
	
	public function add()
	{
		if ($this->request->is('post')) {
			$thread = $this->Threads->newEntity();
			$thread = $this->Threads->patchEntity($thread, $this->request->data);
			if ($this->Threads->save($thread)) {
				return $this->redirect(['action' => 'index']);
			}
			else{
				return $this->redirect(['action' => 'error']);
			}
		}
	}
	
	public function error()
	{
	
	}
}
?>