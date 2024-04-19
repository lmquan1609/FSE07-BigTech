# Chào mừng đến với khoá học của FSE07-BigTech

## Giới thiệu chung
1. Đây là nơi mọi người có thể nộp bài tập và thảo luận về code.
2. Sau mỗi buổi học các bạn sẽ có bài tập về nhà để luyện tập
3. Các bạn có thể tham khảo thêm về cách dùng Git/Github ở đây:  [https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

## Hướng dẫn nộp bài

**LƯU Ý: Các bạn không merge branch của mình vào master branch và không push code trực tiếp lên master branch.**

 1. Nếu đây là lần đầu bạn đến với repo này thì bạn cần clone project này trước
	 ```
	 git clone https://github.com/FSEOrg/FSE07-BigTech.git
	 cd FSE07-BigTech
	 ``` 
 2. Sau mỗi buổi học, các bạn sẽ thấy thư mục mới cho bài tập ở master branch tương ứng với số bài học. Ví dụ: sau bài học số 3, ở master branch sẽ có folder hw03. Trong mỗi folder sẽ có 2 subfolders
	 a. ```livecoding```: chứa các đoạn code demo trong buổi học
	 b. ```homework```: chứa các bài tập về nhà cho buổi học
 3. Các bạn hãy pull code mới nhất từ master branch về máy (bạn hãy chắc chắn mình đang ở ```main``` branch trước khi tiếp tục, có thể kiểm tra branch hiện tại bằng lệnh ```git branch```)
	 ```
	 cd FSE07-BigTech
	 git checkout main
	 git branch  -> hãy kiểm tra bạn đang ở main branch
	 git pull origin main
	   ```
 4. Tại máy của bạn, tạo branch mới với tên thuộc format sau: hw[số bài học]-[github username của bạn]. Tên branch của bạn cần có format này để review. Ví dụ: ```hw02-abcxyz``` nếu như bạn đang làm bài tập cho buổi số 2 và tên github của bạn là *abcxyz* 
	 ```
	 git checkout -b hw02-abcxyz
	 ```
 5. Bạn hãy viết lời giải vào file tương ứng với mỗi bài tập trong slide buổi học và commit tất cả lới giải và push lên remote branch của bạn. Bạn có thể tạo nhiều commit, miễn là bạn push tất cả code của bạn lên repo trước deadline để được review code.
	 ```
	 git branch -> Hãy chắc chắn bạn đang ở branch làm bài tập của bạn, ví dụ hw02-abcxyz
	 git commit -am 'HW02 - Ten Cua Ban'
	 git push origin hw02-abcxyz
	 ```
 6. Truy cập vào link github của repo này, tạo pull request cho branch của bạn và chúng mình sẽ comment vào pull request đó khi cần thiết và chúng ta có thể cùng thảo luận :) Hướng dẫn tạo pull request các bạn có thể xem ở đây: [Link hướng dẫn tạo PR](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request). Hoặc bạn có thể truy cập trực tiếp vào đường link có format sau để tạo PR: 
 ```https://github.com/FSEOrg/FSE07-BigTech/pull/new/<tên branch của bạn>```
# FSE07-BigTech
