<h2>1102. Path With Maximum Minimum Value</h2><h3>Medium</h3><hr><div><p>Given a&nbsp;matrix of integers <code>grid</code>&nbsp;with&nbsp;<code>m</code>&nbsp;rows and <code>n</code>&nbsp;columns, find&nbsp;the <strong>maximum</strong>&nbsp;score&nbsp;of a path starting at&nbsp;<code>[0,0]</code>&nbsp;and ending at <code>[m-1,n-1]</code>.</p>

<p>The <em>score</em> of a path is the <strong>minimum</strong> value in that path.&nbsp; For example, the value of the path 8 →&nbsp; 4 →&nbsp; 5 →&nbsp; 9 is 4.</p>

<p>A <em>path</em> moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/04/23/1313_ex1.JPG" style="width: 70px; height: 59px;"></strong></p>

<pre><strong>Input: </strong><span id="example-input-1-1">[[5,4,5],[1,2,6],[7,4,6]]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<strong>Explanation: </strong>
The path with the maximum score is highlighted in yellow. 
</pre>

<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/04/23/1313_ex2.JPG" style="width: 134px; height: 39px;"></strong></p>

<pre><strong>Input: </strong><span>[[2,2,1,2,2,2],[1,2,2,2,1,2]]</span>
<strong>Output: 2</strong></pre>

<p><strong>Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/04/23/1313_ex3.JPG"></strong></p>

<pre><strong>Input: </strong><span>[[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]</span>
<strong>Output: 3</strong></pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= m, n&nbsp;&lt;= 100</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ol>
</div>