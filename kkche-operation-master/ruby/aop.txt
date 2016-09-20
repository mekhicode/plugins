class TweetsController
  def display_tweets
    puts "tweet tweet tweet"
  end

  def display_users_most_popular_tweets
    display_tweets
  end

  def requires_login(func_name)
    old_method = instance_method(func_name)
    define_method(func_name) do |*args|
      if user_is_logged_in
        old_method.bind(self).call(*args)
      else
        redirect_to_login_page
      end
    end
  end

  display_users_most_popular_tweets = requires_login(:display_users_most_popular_tweets)
end



module M
  def self.before(*names)
    names.each do |name|
      old_name = instance_method(name)
      define_method(name) do |*args, &block|  
      yield
      old_name.bind(self).call(*args, &block)
      end
    end
  end
end

module M
  def hello
    puts "yo"
  end

  def bye
    puts "bum"
  end

  before(*instance_methods) { puts "start" }
end

class C
  include M
end

C.new.bye #=> "start" "bum"
C.new.hello #=> "start" "yo"

